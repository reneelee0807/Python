from abc import ABCMeta, abstractmethod


class Chart(object):
    def __init__(self, chart_type):
        self.chart_type = chart_type

    def make_chart(self):
        self.chart_type.create()
