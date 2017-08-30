import unittest
from math import *
from lineADT import *
from circleADT import *
from pointADT import *
from deque import *

class __main__(unittest.TestCase):
    def test_xcrd_are_equal(self):
        point = PointT(5,2)
        self.assertTrue(point.xcrd() == 5)

    def test_ycrd_are_equal(self):
        point = PointT(5,2)
        self.assertTrue(point.ycrd() == 2)

    def test_dist_are_equal(self):
        point = PointT(5,2)
        point2 = PointT(2,2)
        self.assertTrue(point.dist(point2) == 3)

    def test_rot_for_positive_value(self):
        point = PointT(5,2)
        point.rot(pi/2)
        self.assertTrue((point.xcrd()==-2.0) and (point.ycrd()==5.0))

    def test_rot_for_negative_value(self):
        point = PointT(20,24)
        point.rot(-pi)
        self.assertTrue((point.xcrd()==-20.0) and (point.ycrd()==-24.0) )

    
    def test_rot_for_zero(self):
        point = PointT(50,21)
        point.rot(0)
        self.assertTrue(point.xcrd() == 50 and point.ycrd() == 21)

    def test_rot_for_theta_greater_than_pi(self):
        point = PointT(6,4)
        point.rot(3*pi/2)
        self.assertTrue(point.xcrd() == 4 and point.ycrd() == -6)

    def test_beg_in_lineADT(self):
        point = PointT(5,2)
        point2= PointT(1,1)
        line = LineT(point, point2)
        self.assertTrue((line.beg()).xcrd() == 5 and (line.beg()).ycrd() == 2)
        
    def test_end(self):
        point = PointT(5,2)
        point2= PointT(1,1)
        line = LineT(point, point2)
        self.assertTrue((line.end()).xcrd() == 1 and (line.end()).ycrd() == 1)

    def test_len(self):
        point = PointT(5,0)
        point2= PointT(1,0)
        line = LineT(point, point2)
        self.assertTrue((line.len()) == 4)

    def test_mdpt(self):
        point = PointT(5,0)
        point2= PointT(1,0)
        line = LineT(point, point2)
        self.assertTrue((line.mdpt()).xcrd() == 3 and line.mdpt().ycrd() == 0)

    def test_mdpt(self):
        point = PointT(5,1)
        point2 = PointT(5,1)
        line = LineT(point, point2)
        self.assertTrue((line.mdpt()).xcrd() == 0 and line.mdpt().ycrd() == 0)

    def test_avg_function_in_LineADT(self):
        self.assertTrue(avg(4,2) == 3)

    def test_cen(self):
        circle = CircleT(PointT(5,5), 10)
        self.assertTrue((circle.cen()).xcrd() == 5 and (circle.cen()).ycrd() == 5)
        
    def test_rad(self):
        circle = CircleT(PointT(8,2), 25)
        self.assertTrue(circle.rad() == 25)

    def test_area(self):
        circle = CircleT(PointT(8,2), 25)
        self.assertTrue(circle.area() == pi* 25**2)

    def intersect(self):
        circle = CircleT(PointT(8,2), 25)
        circle2 = CircleT(PointT(100,100), 5)
        self.assertTrue( circle.intersect(circle2) == False)

    def test_connection(self):
        circle = CircleT(PointT(8,2), 25)
        circle2 = CircleT(PointT(10,10), 5)
        self.assertTrue(circle.connection(circle2).beg().xcrd() == 8 and circle.connection(circle2).beg().ycrd() == 2 and circle.connection(circle2).end().xcrd() == 10 and circle.connection(circle2).end().ycrd() == 10)

                        
    def test_force(self):
        circle = CircleT(PointT(8,2), 25)
        circle2 = CircleT(PointT(10,10), 5)
        f = lambda f: f+1
        self.assertTrue(round(circle.force(f)(circle2)) == 1425882.0)

    def test_force_circle_with_force_is_very_small(self):
        circle = CircleT(PointT(1000,100000), 0.00001)
        circle2 = CircleT(PointT(10,10), 5)
        f = lambda f: f+1
        self.assertTrue(round(circle.force(f)(circle2)) == 0)

    def test_insideCircle(self):
        point = PointT(8,9)
        circle2 = CircleT(PointT(8,8), 5)
        self.assertTrue(insideCircle(point ,circle2) == True)

    def test_pushBack(self):
        circle2 = CircleT(PointT(10,10), 5)
        
        Deq.pushBack(circle2)
        self.assertTrue(Deq.back().rad() == circle2.rad())
        
    def test_pushBack_when_queue_is_full(self):
        Deq.popBack()
       
        
        c = CircleT(PointT(10,10), 5)
        for i in range(20):
            Deq.pushBack(c)
        self.assertRaises(Exception, Deq.pushBack, c)

    def test_pushFront(self):
        for i in range(21):
            Deq.popBack()

        
        c = CircleT(PointT(10,10), 5)
        c1 = CircleT(PointT(100,10), 5)
        
        Deq.pushFront(c)
        Deq.pushFront(c1)
        self.assertTrue(Deq.back().rad() == c.rad())

    def test_pushFront_when_queue_is_full(self):
    
        Deq.popBack()
        Deq.popBack()
        
        c = CircleT(PointT(10,10), 5)
        for i in range(21):
            Deq.pushBack(c)
        self.assertRaises(Exception, Deq.pushFront, c)

    def test_popBack(self):
        
           
        c = CircleT(PointT(10,10), 5)
        c1 = CircleT(PointT(100,10), 5)
        Deq.pushFront(c)
        Deq.pushFront(c1)
        self.assertTrue(Deq.popBack().rad() == c.rad())
    
    def test_popBack_when_the_queue_is_empty(self):
        Deq.popBack()
        Deq.popBack()
        self.assertRaises(Exception, Deq.popBack)

    def test_pop_Front(self):
        c = CircleT(PointT(10,10), 5)
        c1 = CircleT(PointT(100,10), 5)
        Deq.pushFront(c)
        Deq.pushFront(c1)
        
        self.assertTrue(Deq.popFront().rad() == c1.rad())

    def test_disjoint(self):
        c = CircleT(PointT(10,10), 5)
        Deq.pushFront(c)

        self.assertTrue(Deq.disjoint() == True)

    def test_sumFx(self):
        
        self.assertTrue(True)
        
if  __name__ == '__main__':
    unittest.main()
