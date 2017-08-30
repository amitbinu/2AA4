package Assignment_3;

import static org.junit.Assert.*;

import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Test;

/**
 * The testing method used is very similar to the one that was used for the previous assignment.
 * Every time an assert statement is used to check whether the expected output is same as the actual output.
 * @author Amit Binu
 *
 */
public class TestPathCalculation {
	
	@Test
	public void testTotalDistance() throws InvalidPositionException { //This method will test the totalDistance method in the PathCalculation module.
		PathT test = new PathT();
		
		try{
			test.add(0, new PointT(0,0));
			test.add(1, new PointT(5,0));
		}
		catch (FullSequenceException | InvalidPositionException | InvalidPointException e) {
			e.printStackTrace();
		}
		assertTrue(PathCalculation.totalDistance(test) == 5.0);
		
		test = new PathT();
		try {
			test.add(0, new PointT(5,5));
			test.add(1, new PointT(10, 5) );
			test.add(2, new PointT(10,10));
			test.add(3, new PointT(5,10));
			test.add(4, new PointT(5,5));
		} 
		catch (FullSequenceException | InvalidPositionException | InvalidPointException e) {
			e.printStackTrace();
		}
		
		assertTrue(PathCalculation.totalDistance(test) == 20.0);
	}

	@Test
	public void testTotalTurns() throws InvalidPositionException {//This method will test the totalTurns method in the PathCalculation module.
		PathT test = new PathT();
		
		try {
			test.add(0, new PointT(0,0));
			test.add(1, new PointT(10, 0) );
			test.add(2, new PointT(15,10));
			test.add(3, new PointT(0,10));
			test.add(4, new PointT(0,0));
		} 
		catch (FullSequenceException | InvalidPositionException | InvalidPointException e) {
			e.printStackTrace();
		}
		
		assertTrue(PathCalculation.totalTurns(test) == 3);
		
		test = new PathT();
		try {
			test.add(0, new PointT(0,0));
			test.add(1, new PointT(5, 0) );
			test.add(2, new PointT(10,5));
			
		} 
		catch (FullSequenceException | InvalidPositionException | InvalidPointException e) {
			e.printStackTrace();
		}
		
		assertTrue(PathCalculation.totalTurns(test) == 1);
	}

	@Test
	public void testEstimatedTime() throws InvalidPositionException {//This method will test the EstimatedTime method in the PathCalculation module.
		PathT test = new PathT();
		
		try {
			test.add(0, new PointT(5,5));
			test.add(1, new PointT(10, 5) );
			test.add(2, new PointT(10,10));
			test.add(3, new PointT(5,10));
			test.add(4, new PointT(5,5));
		} 
		
		catch (FullSequenceException | InvalidPositionException | InvalidPointException e) {
			e.printStackTrace();
		}		
		assertTrue(PathCalculation.estimatedTime(test) == 2.0);
	}
	
	@Test
	public void testExceptions(){ //This method will test the exceptions that were used in the PathCalculation module.
		PathT test = new PathT();
		
		try{
			test.getval(0);
			fail("Expected an InvalidPositionException to be thrown");
		}
		
		catch (InvalidPositionException e) {
			assertTrue(e.getMessage().equals("The given position is invalid !!") );
		}
		
		try {
			test.add(0, new PointT(5, 9));
			test.add(1, new PointT(500, 9)); //This is an invalid point because 500 is bigger than Constants.MAX_X
			fail("Expected an InvalidPointException to be thrown");
		} 
		
		catch (FullSequenceException | InvalidPositionException | InvalidPointException e) {
			assertTrue(e.getMessage().equals("This is an invalid point !!") );
		}
		
		try {
			test.add(0, new PointT(5, 9));
			test.getval(20); //This is an invalid position because 20 is bigger than the size of test.
			fail("Expected an InvalidPositionException to be thrown");
		} 
		
		catch (FullSequenceException | InvalidPositionException | InvalidPointException e) {
			assertTrue(e.getMessage().equals("The given position is invalid !!") );
		}
		
		try{
			test.add(0, new PointT(5, 9));
			test.getval(-1); //This is an invalid position because -1 is less than 0.
			fail("Expected an InvalidPositionException to be thrown");

		}
		catch (FullSequenceException | InvalidPositionException | InvalidPointException e) {
			assertTrue(e.getMessage().equals("The given position is invalid !!") );
		}
		
		test = new PathT();
		try {
			for (int i =0; i < 100; i++){
				test.add(i, new PointT(5, 9));
			}
			test.add(100, new PointT(17, 20));
			fail("Expected an FullSequenceException to be thrown");
		} 
		
		catch (FullSequenceException | InvalidPositionException | InvalidPointException e){
			assertTrue(e.getMessage().equals("The sequence is FULL !!") );
		}	
	}

}
