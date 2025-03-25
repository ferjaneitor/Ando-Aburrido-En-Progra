import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches
import random

# =============================================================================
# 1. PARÁMETROS DEL SISTEMA Y DEL MOTOR
# =============================================================================

np.random.seed(42)
random.seed(42)

num_etapas = 3
masa_por_etapa = 4.0   # [kg]
masa_carga = 25.0      # [kg]
masa_total = num_etapas * masa_por_etapa + masa_carga  # [kg]

g = 9.81  # m/s²

diametro_sprocket_cm = 6.35
radio_sprocket_cm = diametro_sprocket_cm / 2.0
diametro_sprocket_m = diametro_sprocket_cm / 100.0
radio_sprocket_m = radio_sprocket_cm / 100.0

torque_motor_individual = 2.4  # [N·m] por motor
num_motores = 2
torque_total_motor = torque_motor_individual * num_motores  # [N·m]
relacion_transmision = 64
vel_motor_rpm = 5676

vel_motor_rps = vel_motor_rpm / 60.0
vel_salida_rad_s = (vel_motor_rpm * 2.0 * np.pi / 60.0) / relacion_transmision
tau_motor_max = torque_total_motor * relacion_transmision  # [N·m]

torque_carga = masa_total * g * radio_sprocket_m  # [N·m]
I = masa_total * (radio_sprocket_m ** 2)  # [kg·m²]

# =============================================================================
# 2. PARÁMETROS DE SIMULACIÓN
# =============================================================================

t_total = 120.0   # [s]
dt = 0.01
t_array = np.arange(0, t_total, dt)
n_steps = len(t_array)

# Setpoint en cm y conversión a m
setpoint_cm = 192.0
setpoint_m = setpoint_cm / 100.0

max_linear_speed = 0.8846184951  # [m/s]

# =============================================================================
# 3. FUNCIONES DE UTILIDAD
# =============================================================================

def time_to_first_crossing(displacement_m, setpoint_m, t_array):
    for i in range(len(t_array)):
        if displacement_m[i] >= setpoint_m:
            return t_array[i]
    return t_array[-1]

# =============================================================================
# 4. PERFIL DE MOVIMIENTO TRAPEZOIDAL
# =============================================================================

def trapezoidal_profile(t, x0, xf, a_max, v_max):
    d_total = xf - x0
    t_a = v_max / a_max             # Tiempo de aceleración
    d_a = 0.5 * a_max * t_a**2        # Distancia durante la aceleración

    if d_total > 2 * d_a:
        # Perfil trapezoidal
        t_c = (d_total - 2 * d_a) / v_max
        t_total = 2 * t_a + t_c
        if t < t_a:
            x_d = x0 + 0.5 * a_max * t**2
        elif t < t_a + t_c:
            x_d = x0 + d_a + v_max * (t - t_a)
        elif t <= t_total:
            x_d = xf - 0.5 * a_max * (t_total - t)**2
        else:
            x_d = xf
    else:
        # Perfil triangular
        t_a_new = np.sqrt(d_total / a_max)
        t_total = 2 * t_a_new
        if t < t_a_new:
            x_d = x0 + 0.5 * a_max * t**2
        elif t <= t_total:
            x_d = xf - 0.5 * a_max * (t_total - t)**2
        else:
            x_d = xf
    return x_d

# =============================================================================
# 5. SIMULACIÓN DEL SISTEMA CON PID (utilizando perfil trapezoidal)
# =============================================================================

def simulate_pid(Kp, Ki, Kd,
                 alpha=0.8,
                 beta_overshoot=1.0,
                 beta_error_final=0.1,
                 beta_oscillation=0.0,
                 a_max_trap=0.1,
                 v_max_trap=max_linear_speed):
    theta = np.zeros(n_steps)
    omega = np.zeros(n_steps)
    displacement_m = np.zeros(n_steps)

    integral_error = 0.0
    prev_error = 0.0
    filtered_derivative = 0.0
    oscillation_penalty = 0.0

    for i in range(1, n_steps):
        displacement_m[i-1] = radio_sprocket_m * theta[i-1]
        t = i * dt
        x_d = trapezoidal_profile(t, 0, setpoint_m, a_max_trap, v_max_trap)
        current_error = x_d - displacement_m[i-1]

        integral_error += current_error * dt
        raw_derivative = (current_error - prev_error) / dt
        filtered_derivative = alpha * filtered_derivative + (1 - alpha) * raw_derivative

        pid_output = Kp * current_error + Ki * integral_error + Kd * filtered_derivative
        commanded_torque = torque_carga + pid_output

        if commanded_torque < 0:
            commanded_torque = 0
            integral_error -= current_error * dt
        elif commanded_torque > tau_motor_max:
            commanded_torque = tau_motor_max
            integral_error -= current_error * dt

        net_torque = commanded_torque - torque_carga
        alpha_angular = net_torque / I

        omega[i] = omega[i-1] + alpha_angular * dt
        linear_speed = omega[i] * radio_sprocket_m

        if linear_speed > max_linear_speed:
            linear_speed = max_linear_speed
            omega[i] = linear_speed / radio_sprocket_m
        elif linear_speed < -max_linear_speed:
            linear_speed = -max_linear_speed
            omega[i] = linear_speed / radio_sprocket_m

        theta[i] = theta[i-1] + omega[i] * dt

        if i > 1:
            oscillation_penalty += abs(displacement_m[i-1] - displacement_m[i-2])
            
        prev_error = current_error

    displacement_m[-1] = radio_sprocket_m * theta[-1]

    crossing_time = time_to_first_crossing(displacement_m, setpoint_m, t_array)
    max_disp = np.max(displacement_m)
    overshoot = max_disp - setpoint_m if max_disp > setpoint_m else 0.0
    error_final = setpoint_m - displacement_m[-1]

    cost = (crossing_time
            + beta_overshoot * (overshoot ** 2)
            + beta_error_final * (error_final ** 2)
            + beta_oscillation * oscillation_penalty)
    return cost

def simulate_pid_full(Kp, Ki, Kd,
                      alpha=0.8,
                      beta_overshoot=1.0,
                      beta_error_final=0.1,
                      beta_oscillation=0.0,
                      a_max_trap=0.1,
                      v_max_trap=max_linear_speed):
    theta = np.zeros(n_steps)
    omega = np.zeros(n_steps)
    displacement_m = np.zeros(n_steps)
    
    integral_error = 0.0
    prev_error = 0.0
    filtered_derivative = 0.0

    for i in range(1, n_steps):
        displacement_m[i-1] = radio_sprocket_m * theta[i-1]
        t = i * dt
        x_d = trapezoidal_profile(t, 0, setpoint_m, a_max_trap, v_max_trap)
        current_error = x_d - displacement_m[i-1]
        integral_error += current_error * dt

        raw_derivative = (current_error - prev_error) / dt
        filtered_derivative = alpha * filtered_derivative + (1 - alpha) * raw_derivative

        pid_output = Kp * current_error + Ki * integral_error + Kd * filtered_derivative
        commanded_torque = torque_carga + pid_output
        if commanded_torque < 0:
            commanded_torque = 0
            integral_error -= current_error * dt
        elif commanded_torque > tau_motor_max:
            commanded_torque = tau_motor_max
            integral_error -= current_error * dt

        net_torque = commanded_torque - torque_carga
        alpha_angular = net_torque / I
        omega[i] = omega[i-1] + alpha_angular * dt

        linear_speed = omega[i] * radio_sprocket_m
        if linear_speed > max_linear_speed:
            linear_speed = max_linear_speed
            omega[i] = linear_speed / radio_sprocket_m
        elif linear_speed < -max_linear_speed:
            linear_speed = -max_linear_speed
            omega[i] = linear_speed / radio_sprocket_m

        theta[i] = theta[i-1] + omega[i] * dt
        prev_error = current_error
        
    displacement_m[-1] = radio_sprocket_m * theta[-1]
    return displacement_m

# =============================================================================
# 6. PARÁMETROS PID MANUALES
# =============================================================================
# Ajusta manualmente los parámetros PID y de control aquí:
Kp = 0.20    # Valor manual para Kp
Ki = 0.2   # Valor manual para Ki
Kd = 0.0    # Valor manual para Kd

alpha_derivative = 0.8
beta_overshoot_val = 1.0
beta_error_final_val = 0.9
beta_oscillation_val = 0.8

# =============================================================================
# 7. ANIMACIÓN DEL MOVIMIENTO TELESCÓPICO
# =============================================================================

def animate_telescopic_elevator(displacement_m, t_array, num_etapas, setpoint_m):
    """
    Anima el movimiento del elevador telescópico dividiendo el desplazamiento
    en 'num_etapas'. Cada etapa se representa como un rectángulo que se extiende
    hasta un máximo de (setpoint_m/num_etapas) cuando está completamente extendida.
    La carga se muestra como un rectángulo rojo en la parte superior.
    """
    # Longitud máxima que puede extenderse cada etapa
    L_max = setpoint_m / num_etapas

    fig, ax = plt.subplots()
    ax.set_xlim(-0.5, 1.5)
    ax.set_ylim(0, setpoint_m * 1.2)
    ax.set_xlabel("Posición (arbitraria)")
    ax.set_ylabel("Altura (m)")
    ax.set_title("Animación del Elevador Telescópico")

    # Colores para cada etapa
    colors = ['skyblue', 'lightgreen', 'khaki']
    segments_patches = []
    for i in range(num_etapas):
        # Se crean rectángulos con altura inicial 0
        rect = patches.Rectangle((0, 0), 1, 0, fc=colors[i % len(colors)], ec='black')
        segments_patches.append(rect)
        ax.add_patch(rect)

    # La carga se representa con un rectángulo rojo (altura fija)
    carga_altura = 0.2
    load_patch = patches.Rectangle((0, 0), 1, carga_altura, fc='red', ec='black')
    ax.add_patch(load_patch)

    def update(frame):
        d = displacement_m[frame]  # Desplazamiento total en este instante
        remaining = d
        y_pos = 0
        for rect in segments_patches:
            extension = min(remaining, L_max)
            rect.set_xy((0, y_pos))
            rect.set_width(1)
            rect.set_height(extension)
            y_pos += extension
            remaining -= extension
        # Ubicar la carga sobre el último segmento
        load_patch.set_xy((0, y_pos))
        return segments_patches + [load_patch]

    ani = animation.FuncAnimation(fig, update, frames=len(t_array), interval=dt*1000, blit=True)
    plt.show()

# =============================================================================
# 8. EJECUCIÓN PRINCIPAL
# =============================================================================

if __name__ == "__main__":
    # Parámetros del perfil trapezoidal
    a_max_trap = 0.1  # [m/s²]
    v_max_trap = max_linear_speed  # [m/s]

    # Ejecuta la simulación usando los parámetros PID manuales
    disp_m = simulate_pid_full(
        Kp, Ki, Kd,
        alpha=alpha_derivative,
        beta_overshoot=beta_overshoot_val,
        beta_error_final=beta_error_final_val,
        beta_oscillation=beta_oscillation_val,
        a_max_trap=a_max_trap,
        v_max_trap=v_max_trap
    )
    disp_cm = disp_m * 100.0

    # Grafica la respuesta
    plt.figure(figsize=(8, 5))
    plt.plot(t_array, disp_cm, label="Desplazamiento (cm)")
    desired_profile = [trapezoidal_profile(t, 0, setpoint_m, a_max_trap, v_max_trap)*100.0 for t in t_array]
    plt.plot(t_array, desired_profile, 'k--', label="Trayectoria deseada")
    plt.xlabel("Tiempo [s]")
    plt.ylabel("Desplazamiento [cm]")
    plt.title("Respuesta con PID y perfil trapezoidal")
    plt.legend()
    plt.grid(True)
    plt.show()

    # Mostrar la animación del elevador telescópico
    animate_telescopic_elevator(disp_m, t_array, num_etapas, setpoint_m)
