package Assignment_3;


/**
 * <b> The purpose of this class is to generate a point which will have its own coordinate values </b>
 * @author Amit Binu
 * @since 2017-03-20
 */
public class PointT {

	protected double xc;
	protected double yc;

	/**The constructor will take two double values that represents the coordinate values.
	 * 
	 * @param x is a double value that represents the x-coordinate of the point.
	 * @param y is a double value that represents the y-coordinate of the point.
	 * @throws InvalidPointException If the value of x is equal to or bigger than Constants.MAX_X this exception will be thrown. It will also throw this exception
	 * if the value of y is equal to or bigger than Constants.MAX_Y.
	 */
	public PointT(double x, double y) throws InvalidPointException{
		xc = x;
		yc = y;
		
		if (! (0 <= x && x <= Constants.MAX_X) || !(0<= y && y<= Constants.MAX_Y)){

			throw new InvalidPointException();
		}
	}

	/**This method will return the value of the point's x-coordinate.
	 * 
	 * @return a double value that represents the point's x-coordinate.
	 */
	public double xcrd(){
		return xc;
	}
	
	/**This method will return the value of the point's y-coordinate.
	 * 
	 * @return a double value that represents the point's y-coordinate.
	 */
	public double ycrd(){
		return yc;
	}
	
	/**THis method will calculate and return the distance between two points.
	 * 
	 * @param p is a PointT object which will have its own x-coordinate and y-coordinate.
	 * @return a double value that represents the distance between original point and the point <b> p </b>.
	 */
	public double dist(PointT p){
		return Math.sqrt(Math.pow((this.xc - p.xc) , 2) + Math.pow((this.yc - p.yc), 2));
	}
}
