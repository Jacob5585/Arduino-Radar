from radar_graph import PolarPlot
import read_arduino_data

def main():
    radar_graph = PolarPlot(100.0, 150)

    while radar_graph.running:
        try:
            angle, distance = read_arduino_data.process_data()
            radar_graph.dists[int(angle)] = distance
            radar_graph.update_plot(angle, radar_graph.dists)
        
        except KeyboardInterrupt:
            plt.close('all')
            print('Keyboard Interrupt')
            exit()

if __name__ == "__main__":
    main()