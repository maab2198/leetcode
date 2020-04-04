class Solution:
    def checkOverlap(self, radius: int, x_center: int, y_center: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        if y_center < y1:
            if x_center < x1:
                return (x_center-x1)**2 + (y_center-y1)**2 <= radius**2
            if x_center > x2:
                return (x_center-x2)**2 + (y_center-y1)**2 <= radius**2
            return abs(y1-y_center) <=radius
        elif y_center > y2:
            if x_center < x1:
                return (x_center-x1)**2 + (y_center-y2)**2 <= radius**2
            if x_center > x2:
                return (x_center-x2)**2 + (y_center-y2)**2 <= radius**2
            return abs(y2-y_center) <=radius
        elif x_center < x1:
                return abs(x1-x_center) <=radius
        elif x_center >x2:
                return abs(x_center -x2) <=radius
        return True

        