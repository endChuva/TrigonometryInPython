import os
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
from termcolor import colored

def to_radians(degrees):
    return math.radians(degrees)

def to_degrees(radians):
    return math.degrees(radians)

def sine(angle, in_degrees=True):
    if in_degrees:
        angle = to_radians(angle)
    return math.sin(angle)

def cosine(angle, in_degrees=True):
    if in_degrees:
        angle = to_radians(angle)
    return math.cos(angle)

def tangent(angle, in_degrees=True):
    if in_degrees:
        angle = to_radians(angle)
    return math.tan(angle)

def arcsine(value, in_degrees=True):
    angle = math.asin(value)
    if in_degrees:
        return to_degrees(angle)
    return angle

def arccosine(value, in_degrees=True):
    if -1 <= value <= 1:
        angle = math.acos(value)
        if in_degrees:
            return to_degrees(angle)
        return angle
    else:
        return "Error: Value out of range. Must be between -1 and 1."

def arctangent(value, in_degrees=True):
    angle = math.atan(value)
    if in_degrees:
        return to_degrees(angle)
    return angle

def analysis_and_visualization():
    fig, ax = plt.subplots()
    plt.subplots_adjust(left=0.1, bottom=0.3)

    x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
    initial_amplitude = 1
    initial_frequency = 1
    initial_phase = 0

    def update_graphs(amplitude, frequency, phase):
        ax.clear()
        y_sin = amplitude * np.sin(frequency * x + phase)
        y_cos = amplitude * np.cos(frequency * x + phase)
        y_tan = amplitude * np.tan(frequency * x + phase)
        
        ax.plot(x, y_sin, label='Sine', color='blue')
        ax.plot(x, y_cos, label='Cosine', color='green')
        ax.plot(x, y_tan, label='Tangent', color='red')
        
        ax.axhline(0, color='black', linewidth=0.5)
        ax.axvline(0, color='black', linewidth=0.5)
        ax.legend()
        ax.set_ylim(-2, 2)
        ax.set_title(f'Trigonometric Functions\nAmplitude: {amplitude}, Frequency: {frequency}, Phase: {phase} radians')
        plt.draw()

    update_graphs(initial_amplitude, initial_frequency, initial_phase)

    ax_amp = plt.axes([0.1, 0.2, 0.65, 0.03])
    ax_freq = plt.axes([0.1, 0.15, 0.65, 0.03])
    ax_phase = plt.axes([0.1, 0.1, 0.65, 0.03])

    slider_amp = Slider(ax_amp, 'Amplitude', 0.1, 5.0, valinit=initial_amplitude)
    slider_freq = Slider(ax_freq, 'Frequency', 0.1, 5.0, valinit=initial_frequency)
    slider_phase = Slider(ax_phase, 'Phase', -np.pi, np.pi, valinit=initial_phase)

    def update(val):
        update_graphs(slider_amp.val, slider_freq.val, slider_phase.val)

    slider_amp.on_changed(update)
    slider_freq.on_changed(update)
    slider_phase.on_changed(update)

    resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
    button = Button(resetax, 'Reset', color='lightgoldenrodyellow', hovercolor='0.975')

    def reset(event):
        slider_amp.reset()
        slider_freq.reset()
        slider_phase.reset()

    button.on_clicked(reset)

    plt.show()

def motion_simulation():
    def simulate_motion(initial_velocity, angle_deg):
        g = 9.81
        angle_rad = math.radians(angle_deg)
        v_x = initial_velocity * math.cos(angle_rad)
        v_y = initial_velocity * math.sin(angle_rad)
        t_flight = 2 * v_y / g
        t = np.linspace(0, t_flight, num=500)
        x = v_x * t
        y = v_y * t - 0.5 * g * t**2

        fig, ax = plt.subplots()
        ax.plot(x, y)
        ax.set_title('Projectile Motion')
        ax.set_xlabel('Distance (m)')
        ax.set_ylabel('Height (m)')
        ax.grid(True)
        plt.show()

    initial_velocity = float(input("Enter the initial velocity (m/s): "))
    angle_deg = float(input("Enter the launch angle (degrees): "))
    simulate_motion(initial_velocity, angle_deg)

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(colored('''     
        ████████╗██████╗ ██╗ ██████╗  ██████╗ ███╗   ██╗ ██████╗ ███╗   ███╗███████╗████████╗██████╗ ██╗   ██╗
        ╚══██╔══╝██╔══██╗██║██╔════╝ ██╔═══██╗████╗  ██║██╔═══██╗████╗ ████║██╔════╝╚══██╔══╝██╔══██╗╚██╗ ██╔╝
           ██║   ██████╔╝██║██║  ███╗██║   ██║██╔██╗ ██║██║   ██║██╔████╔██║█████╗     ██║   ██████╔╝ ╚████╔╝ 
           ██║   ██╔══██╗██║██║   ██║██║   ██║██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══╝     ██║   ██╔══██╗  ╚██╔╝  
           ██║   ██║  ██║██║╚██████╔╝╚██████╔╝██║ ╚████║╚██████╔╝██║ ╚═╝ ██║███████╗   ██║   ██║  ██║   ██║   
           ╚═╝   ╚═╝  ╚═╝╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝  
           
        matheusmrq.github.io/Profile''', 'cyan'))
    print('\n   Choose your option: [1]Trigonometric Calculator   [2]Analysis and Visualization   [3]Coming Soon...')
    opc = int(input('          '))
    if opc == 1:
        print("\nComplete Trigonometric Calculator")
        print("1. Sine")
        print("2. Cosine")
        print("3. Tangent")
        print("4. Arcsine")
        print("5. Arccosine")
        print("6. Arctangent")
        print("7. Convert Degrees to Radians")
        print("8. Convert Radians to Degrees")
        print("9. Exit")
        
        choice = int(input("Choose an option: "))
        
        if choice == 1:
            angle = float(input("Enter angle: "))
            unit = input("Is the angle in degrees (y/n)? ").lower() == 'y'
            print(f"Sine: {sine(angle, unit)}")
            pessonly = input('Press ENTER to continue...')
        elif choice == 2:
            angle = float(input("Enter angle: "))
            unit = input("Is the angle in degrees (y/n)? ").lower() == 'y'
            print(f"Cosine: {cosine(angle, unit)}")
            pessonly = input('Press ENTER to continue...')
        elif choice == 3:
            angle = float(input("Enter angle: "))
            unit = input("Is the angle in degrees (y/n)? ").lower() == 'y'
            print(f"Tangent: {tangent(angle, unit)}")
            pessonly = input('Press ENTER to continue...')
        elif choice == 4:
            value = float(input("Enter value: "))
            unit = input("Do you want the result in degrees (y/n)? ").lower() == 'y'
            print(f"Arcsine: {arcsine(value, unit)}")
            pessonly = input('Press ENTER to continue...')
        elif choice == 5:
            value = float(input("Enter value: "))
            unit = input("Do you want the result in degrees (y/n)? ").lower() == 'y'
            print(f"Arccosine: {arccosine(value, unit)}")
            pessonly = input('Press ENTER to continue...')
        elif choice == 6:
            value = float(input("Enter value: "))
            unit = input("Do you want the result in degrees (y/n)? ").lower() == 'y'
            print(f"Arctangent: {arctangent(value, unit)}")
            pessonly = input('Press ENTER to continue...')
        elif choice == 7:
            degrees = float(input("Enter angle in degrees: "))
            print(f"Radians: {to_radians(degrees)}")
            pessonly = input('Press ENTER to continue...')
        elif choice == 8:
            radians = float(input("Enter angle in radians: "))
            print(f"Degrees: {to_degrees(radians)}")
            pessonly = input('Press ENTER to continue...')
        elif choice == 9:
            opc = 0
        else:
            print("Invalid option. Please try again.")
            pessonly = input('Press ENTER to continue...')
    
    elif opc == 2:
        analysis_and_visualization()
        pessonly = input('Press ENTER to continue...')

    else:
        print('Soon...')
        pessonly = input('Press ENTER to continue...')
