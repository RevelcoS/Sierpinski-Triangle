import tkinter as tk
from math import sqrt, cos, sin, radians


class Triangle:

    def __init__(self, canvas, width, height):
        self.canvas = canvas

        self.w = width
        self.h = ( sqrt(3) * self.w ) / 2
        
        self._set_white_trig(self.w, self.h, height)
        self.vlength = self.w / 2
        self.points = [(self.w / 2, height)]

        self.gen = 1


    def _set_white_trig(self, w, h, ah):
        points = [
            0, ah,
            w, ah,
            w / 2, ah - h]
    
        self.canvas.create_polygon( points, fill="white" )


    def _rotate_vector(self, x1, y1, angle):
        x2 = x1 * cos(angle) - y1 * sin(angle)
        y2 = x1 * sin(angle) + y1 * cos(angle)
        return (x2, y2)


    def next_gen(self):
        vector = (0, self.vlength)
        right_vector = self._rotate_vector(vector[0], vector[1], radians(330))
        left_vector = self._rotate_vector(vector[0], vector[1], radians(30))

        new_vlength = self.vlength / 2

        new_points = []
        for point in self.points:
            x, y = point
            trig_points = [
                x, y,
                x - left_vector[0], y - left_vector[1],
                x - right_vector[0], y - right_vector[1]]

            self.canvas.create_polygon( trig_points, fill="black" )


            append_points = [
                (x - new_vlength, y),
                (x + new_vlength, y),
                (x, y - (self.h / (2 ** self.gen)))]

            new_points.extend(append_points)


        self.points = new_points
        self.vlength = new_vlength
        self.gen += 1