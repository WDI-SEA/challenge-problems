# There is a robot starting at the position (0, 0), the origin, on a 2D plane. Given a sequence of its moves, judge if this robot ends up at (0, 0) after it completes its moves.

# You are given a string moves that represents the move sequence of the robot where moves[i] represents its ith move. Valid moves are 'R' (right), 'L' (left), 'U' (up), and 'D' (down).

# Return true if the robot returns to the origin after it finishes all of its moves, or false otherwise.

# Note: The way that the robot is "facing" is irrelevant. 'R' will always make the robot move to the right once, 'L' will always make it move left, etc. Also, assume that the magnitude of the robot's movement is the same for each move.


class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        upCount = 0
        downCount = 0
        rightCount = 0
        leftCount = 0
        for i in moves:
            if i == "U":
                upCount += 1
            elif i == "D":
                downCount += 1
            elif i == "R":
                rightCount += 1
            elif i == "L":
                leftCount +=1
        return leftCount == rightCount and upCount == downCount