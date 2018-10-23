import miio
from influx_line_protocol import Metric


class XiaomiAirPurifier:

    def get_metric(self, ip):
        token = self.__discover_token(ip)
        data = miio.airpurifier.AirPurifier(ip, token).status()
        metric = Metric("xiaomi-air-purifier")

        metric.add_value("is_on", data.power == 'on')
        metric.add_value("child_lock", data.child_lock)
        metric.add_value("aqi", data.aqi)
        metric.add_value("filter_hours_used", data.filter_hours_used)
        metric.add_value("filter_life_remaining", data.filter_life_remaining)
        metric.add_value("humidity", data.humidity)
        metric.add_value("illuminance", data.illuminance)
        metric.add_value("motor1_speed", data.motor_speed)
        metric.add_value("motor2_speed", data.motor2_speed)
        metric.add_value("purify_volume", data.purify_volume)
        metric.add_value("temperature", data.temperature)
        metric.add_value("use_time", data.use_time)

        return metric

    def __discover_token(self, ip):
        data = miio.device.Device.discover(ip)
        if data is None:
            raise Exception("Device not found, or it's not supported")

        return data.checksum.hex()
