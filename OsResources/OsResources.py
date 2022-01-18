import psutil

class OS_Resources(object):

    ###########
    #---CPU---#
    ###########

    #procentul utilizarii CPU
    def get_cpu_percent(self, interval, percpu):
        cpu_percent=psutil.cpu_percent(interval, percpu)
        return cpu_percent

    #timpii CPU sistem ca o tupla
    def get_cpu_times(self, percpu):
        cpu_times=psutil.cpu_times(percpu)
        return cpu_times

    #procentul timpilor CPU sistem ca o tupla
    def get_cpu_times_percent(self, interval, percpu):
        cpu_times_percent=psutil.cpu_times_percent(interval, percpu)
        return cpu_times_percent

    #nr. de nuclee de pe procesor (fizice sau logice)
    def get_cpu_count(self, logical):
        cpu_count=psutil.cpu_count(logical)
        return cpu_count

    #frecventa CPU ca o tupla care include frecventele curente, minime si maxime
    #windows nu poate obtine frecventa per nucleu
    def get_cpu_freq(self,percpu):
        percpu=False
        cpu_freq=psutil.cpu_freq(percpu)
        return cpu_freq

    #statistici CPU (nr. schimbari context de la pornire, nr. de intreruperi de la pornire, numărul de întreruperi software de la pornire,numărul de apeluri de sistem de la pornire) ca o tupla
    def get_cpu_stats(self):
        cpu_stats=psutil.cpu_stats()
        return cpu_stats

    #sarcina medie a sistemului in ultimele 1, 5 si 15 min ca o tupla
    def get_load_avg(self):
        cpu_load_avg=psutil.getloadavg()
        return cpu_load_avg

    ##############
    #---MEMORY---#
    ##############

    #utilizarea memoriei sistemului in octeti ca o tupla
    def get_virtual_memory(self):
        virtual_memory=psutil.virtual_memory()
        return virtual_memory

    #statistici ale swap memory ca o tupla
    def get_swap_memory(self):
        swap_memory=psutil.swap_memory()
        return swap_memory

    #############
    #---DISKS---#
    #############

    #detaliile tuturor partitiilor de disc montate ca o lista de tuple
    def get_disk_partitions(self, all):
        disk_partitions=psutil.disk_partitions(all)
        return disk_partitions

    #ofera statistici de utilizare a discului ca o tupla pentru o cale data
    def get_disk_usage(self, path):
        disk_usage=psutil.disk_usage(path)
        return disk_usage

    #statistici i/o pe disc la nivelul  intregului sistem ca o tupla
    def get_disk_io_counters(self, perdisk, nowrap):
        disk_io_counters=psutil.disk_io_counters(perdisk, nowrap)
        return disk_io_counters

    ###############
    #---NETWORK---#
    ###############

    #statisticile i/o ale retelei la nivel de sistem ca o tupla
    def get_net_io_counters(self, pernic, nowrap):
        net_io_counters=psutil.net_io_counters(pernic,nowrap)
        return net_io_counters

    #conexiunile soket la nivel de sistem ca o lista de tuple
    def get_net_connections(self, kind):
        net_connections=psutil.net_connections(kind)
        return net_connections

    ###############
    #---SENSORS---#
    ###############

    #temperaturile hardware
    def get_sensors_temperatures(self,fahrenheit):
        sensors_temperatures=psutil.sensors_temperatures(fahrenheit)
        return sensors_temperatures

    #viteza ventilatoarelor hardware
    def get_sensors_fans(self):
        sensors_fans=psutil.sensors_fans()
        return sensors_fans

    #informatii despre starea bateriei
    def get_sensors_battery(self):
        sensors_battery=psutil.sensors_battery()
        return sensors_battery

    #############
    #---OTHER---#
    #############

    #timpul de pornire a sistemului exprimat în secunde
    def get_boot_time(self):
        boot_time=psutil.boot_time()
        return boot_time

    #utilizatorii conectați în prezent la sistem ca o listă de tuple
    def get_users(self):
        users=psutil.users()
        return users

    function_name=[]

    function_name.append(get_cpu_percent.__name__)
    function_name.append(get_cpu_times.__name__)
    function_name.append(get_cpu_times_percent.__name__)
    function_name.append(get_cpu_count.__name__)
    function_name.append(get_cpu_freq.__name__)
    function_name.append(get_cpu_stats.__name__)
    function_name.append(get_load_avg.__name__)
    function_name.append(get_virtual_memory.__name__)
    function_name.append(get_swap_memory.__name__)
    function_name.append(get_disk_partitions.__name__)
    function_name.append(get_disk_usage.__name__)
    function_name.append(get_disk_io_counters.__name__)
    function_name.append(get_net_io_counters.__name__)
    function_name.append(get_net_connections.__name__)
    function_name.append(get_sensors_temperatures.__name__)
    function_name.append(get_sensors_fans.__name__)
    function_name.append(get_sensors_battery.__name__)
    function_name.append(get_boot_time.__name__)
    function_name.append(get_users.__name__)

    def get_function_name(self):
        return self.function_name

if __name__ == '__main__':
    print ("ma ta")