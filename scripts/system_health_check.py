
import time
import shutil
import logging

logging.basicConfig(
    filename="system_health.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def get_cpu_usage():
    with open("/proc/stat", "r") as file:
        values = list(map(int, file.readline().split()[1:]))

    idle = values[3] + values[4]
    total = sum(values)

    time.sleep(1)

    with open("/proc/stat", "r") as file:
        new_values = list(map(int, file.readline().split()[1:]))

    new_idle = new_values[3] + new_values[4]
    new_total = sum(new_values)

    total_diff = new_total - total
    idle_diff = new_idle - idle

    if total_diff == 0:
        return 0.0

    return round((1 - idle_diff / total_diff) * 100, 2)


def get_memory_usage():
    memory = {}

    with open("/proc/meminfo", "r") as file:
        for line in file:
            key, value = line.split(":", 1)
            memory[key] = int(value.strip().split()[0])

    total = memory["MemTotal"]
    available = memory["MemAvailable"]

    used_percent = ((total - available) / total) * 100

    return round(used_percent, 2)


def get_disk_usage():
    disk = shutil.disk_usage("/")

    used_percent = (disk.used / disk.total) * 100

    return round(used_percent, 2)


def check_status(name, usage, threshold):
    if usage >= threshold:
        print(f"WARNING: {name} usage is high!")
        logging.warning(f"{name} usage is high: {usage}%")
    else:
        print(f"OK: {name} usage is normal.")
        logging.info(f"{name} usage is normal: {usage}%")

def main():
    print("=" * 40)
    print("       SYSTEM HEALTH MONITOR")
    print("=" * 40)

    cpu = get_cpu_usage()
    memory = get_memory_usage()
    disk = get_disk_usage()

    print(f"CPU Usage:    {cpu}%")
    print(f"Memory Usage: {memory}%")
    print(f"Disk Usage:   {disk}%")

    print("-" * 40)

    check_status("CPU", cpu, 80)
    check_status("Memory", memory, 85)
    check_status("Disk", disk, 85)

    print("=" * 40)


if __name__ == "__main__":
    main()
