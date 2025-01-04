import matplotlib
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import numpy as np

class PolarPlot:
    def __init__(self, radius_max, dpi):
        matplotlib.use('TkAgg')
        self.fig = plt.figure(facecolor='k')
        self.axis = self.fig.add_subplot(111, polar=True, facecolor='#006d70')
        self.radius_max = radius_max
        self.dpi = dpi
        self.dists = np.ones((len(np.arange(0, 181, 1)),))
        self.running = True
        self.setup_plot()

        #Create Buttons to stop program
        stop_button = plt.axes([(1 - .1) / 2, 0.01, .1, 0.05])
        self.button = Button(stop_button, 'Stop Program')
        self.button.on_clicked(self.stop_program)

        # Toolbar exit button will stop program
        self.fig.canvas.mpl_connect('close_event', self.stop_program)
        
        self.angles = np.arange(0, 181, 1) # Degrees
        self.theta = self.angles * (np.pi / 180.0) # Radians
        self.pols, = self.axis.plot([],linestyle='',marker='o',markerfacecolor = 'w', markeredgecolor='#EFEFEF',markeredgewidth=1.0, markersize=10.0,alpha=0.9)
        self.radar_sweep, = self.axis.plot([],color='w', linewidth=4.0)

    def setup_plot(self):
        win = self.fig.canvas.manager.window 
        screen_res = win.wm_maxsize()
        self.fig.set_dpi(self.dpi)

        self.fig.set_size_inches(screen_res[0] / self.fig.get_dpi(), screen_res[1] / self.fig.get_dpi())
        self.axis.set_position([-0.05,-0.05,1.1,1.05])

        self.axis.set_ylim([0.0, self.radius_max])
        self.axis.set_xlim([0.0, np.pi])

        self.axis.tick_params(axis='both', colors='w')
        self.axis.grid(color='w', alpha=0.5)

        self.axis.set_rticks(np.linspace(0.0, self.radius_max, 5))
        self.axis.set_thetagrids(np.linspace(0.0, 180.0, 10))

        # Center the plot
        plot_res = self.fig.get_window_extent().bounds
        win.wm_geometry('+{0:1.0f}+{1:1.0f}'.format((screen_res[0] / 2.0) - (plot_res[2] / 2.0), (screen_res[1] / 2.0) - (plot_res[3] / 2.0)))

        # Remove toolbar
        self.fig.canvas.toolbar.pack_forget()

    def update_plot(self, angle, dists):
        #update plot
        self.pols.set_data(self.theta, dists)
        self.radar_sweep.set_data(np.repeat(angle * (np.pi / 180.0), 2), np.linspace(0.0, self.radius_max, 2))  

        # Only redraw the updated parts of the plot
        self.axis.draw_artist(self.pols)
        self.axis.draw_artist(self.radar_sweep)

        # Redraw only the updated region of the canvas
        self.fig.canvas.flush_events()

        # Pause to allow for updates
        plt.pause(0.1)

    def stop_program(self, event):
        plt.close('all')
        self.running = False

    def show(self):
        self.fig.show()

if __name__ == "__main__":
    angle = 0
    increment = 1
    distance = np.random.uniform(0, 100)
    polar_plot = PolarPlot(100.0, 150)

    while polar_plot.running:          
        try:
            change = np.random.uniform(-5, 5)
            distance += change
            
            polar_plot.dists[int(angle)] = distance
            polar_plot.update_plot(angle, polar_plot.dists)
            
            angle += increment
            if angle >= 180:
                increment = -.5  
            elif angle <= 0:
                increment = .5

        except KeyboardInterrupt:
            plt.close('all')
            print('Keyboard Interrupt')
            exit()
