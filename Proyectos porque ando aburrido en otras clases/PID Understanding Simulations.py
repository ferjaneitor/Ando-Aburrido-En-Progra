import numpy as np
import matplotlib.pyplot as plt

def simulate_pid(Kp, Ki, Kd, setpoint=1.0, t_end=10, dt=0.01):
    """
    Simula un controlador PID aplicado a un sistema de primer orden.

    Parámetros:
      - Kp: ganancia proporcional.
      - Ki: ganancia integral.
      - Kd: ganancia derivativa.
      - setpoint: valor deseado de salida.
      - t_end: tiempo total de simulación.
      - dt: paso de tiempo.
      
    Retorna:
      - t: vector de tiempos.
      - x: salida del sistema.
      - u: señal de control.
      - error: error en cada instante.
    """
    t = np.arange(0, t_end, dt)
    n = len(t)
    x = np.zeros(n)       # Salida del sistema
    u = np.zeros(n)       # Acción de control
    error = np.zeros(n)   # Error entre setpoint y salida
    integral = 0.0        # Término integral acumulado
    previous_error = 0.0  # Error anterior para el cálculo derivativo

    for i in range(1, n):
        # Calculamos el error en el instante actual
        error[i] = setpoint - x[i-1]
        
        # Acumulamos el error (integral)
        integral += error[i] * dt
        
        # Calculamos el término derivativo (cambio del error)
        derivative = (error[i] - previous_error) / dt
        
        # Calculamos la señal de control con la fórmula del PID
        u[i] = Kp * error[i] + Ki * integral + Kd * derivative
        
        # Actualizamos la salida del sistema: dx/dt = -x + u
        x[i] = x[i-1] + dt * (-x[i-1] + u[i])
        
        # Actualizamos el error anterior
        previous_error = error[i]
        
    return t, x, u, error

def plot_pid(Kp, Ki, Kd, setpoint=1.0, t_end=10, dt=0.01):
    """
    Ejecuta la simulación y grafica la respuesta del sistema controlado por PID.
    Se muestran dos gráficos:
      - La salida del sistema frente al tiempo.
      - La acción de control aplicada.
    """
    t, x, u, error = simulate_pid(Kp, Ki, Kd, setpoint, t_end, dt)
    
    plt.figure(figsize=(12, 8))
    
    # Gráfico de la salida del sistema
    plt.subplot(2, 1, 1)
    plt.plot(t, x, label='Salida del sistema (x)')
    plt.axhline(setpoint, color='r', linestyle='--', label=f'Setpoint ({setpoint})')
    plt.title('Respuesta del Sistema con Control PID')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Salida (x)')
    plt.legend()
    plt.grid(True)
    
    # Gráfico de la acción de control
    plt.subplot(2, 1, 2)
    plt.plot(t, u, label='Acción de control (u)', color='orange')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Señal de Control (u)')
    plt.legend()
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()

# ------------------------------
# Parámetros a modificar directamente en el código:
Kp = 0.5    # Ganancia proporcional
Ki = 0.0    # Ganancia integral
Kd = 0.0    # Ganancia derivativa

setpoint = 1.0   # Valor deseado de salida
t_end = 10       # Tiempo total de simulación (segundos)
dt = 0.01        # Paso de tiempo

# Ejecuta la simulación y muestra los gráficos
plot_pid(Kp, Ki, Kd, setpoint, t_end, dt)
