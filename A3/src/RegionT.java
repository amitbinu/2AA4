package Assignment_3;
/**
 * <b> The purpose of this class is to generate a region which will have its left-bottom point, width and height </b>
 * @author Amit Binu
 * @since 2017-03-20
 */
public class RegionT {

	protected PointT lower_left;
	protected double width;
	protected double height;
	
	/**The constructor transit the values in its parameters to the appropriate state variables.
	 * 
	 * @param p is a PointT object that represents the lower-left point of the region.
	 * @param w is a double value that represents the width of the region.
	 * @param h is a double value that represents the height of the region.
	 * @throws InvalidRegionException if the region's corner points' x-coordinate are equal to / bigger than Constants.MAX_X, this exception will be thrown.It will also throw this exception if the region's corner's point's y-coordinate is bigger than Constants.MAX_Y.
	 */
	public RegionT(PointT p,double w, double h) throws InvalidRegionException{
		lower_left = p;
		width= w;
		height = h;
		if (!(w > 0 && h >0 && (p.xcrd() +w) <= Constants.MAX_X && (p.ycrd() + h) <= Constants.MAX_Y)){
			throw new InvalidRegionException();
		}
	}
	
	/**This method will check if the entered PointT object p is in the region or not. The point can miis the region by Constants.TOLERANCE level.
	 * 
	 * @param p is a PointT object that this method will use to check whether it is in the region or not.
	 * @return a boolean value true if the PointT p is in the region and if it is not then it will return false.
	 */
	public Boolean  pointInRegion(PointT p){
		boolean check_for_x = p.xcrd() < lower_left.xcrd() || p.xcrd() > (lower_left.xcrd() + width);
		
		boolean check_for_y = p.ycrd() < lower_left.ycrd() || p.ycrd() > (lower_left.ycrd() + height);
		
		/**The if statement will be implemented only if the point is outside the region.
		 * 
		 */
		if (check_for_x || check_for_y){
			
			try {
				for (int i = 0; i < Region().length; i++){
					if(p.dist(Region()[i]) <= Constants.TOLERANCE){
						return true;
					}
				}
			} catch (InvalidPointException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			
			if (Math.abs(p.xcrd() - lower_left.xcrd())  == Constants.TOLERANCE && lower_left.ycrd() <=  p.ycrd() && p.ycrd() <= lower_left.ycrd()+height){
				return true;
			}
			
			if (Math.abs(p.xcrd() - (lower_left.xcrd()+width) )  == Constants.TOLERANCE && lower_left.ycrd() <=  p.ycrd() && p.ycrd() <= lower_left.ycrd()+height){
				return true;
			}
			
			if (Math.abs(p.ycrd() - lower_left.ycrd())  == Constants.TOLERANCE && lower_left.xcrd() <=  p.xcrd() && p.xcrd() <= lower_left.xcrd()+width){
				return true;
			}
			
			if (Math.abs(p.ycrd() - (lower_left.ycrd()+height))  == Constants.TOLERANCE && lower_left.xcrd()<=  p.xcrd() && p.xcrd() <= lower_left.xcrd()+width){
				return true;
			}
			
			else
				return false;
			
			
		}
		return true;
	}
	

	/**This is a local function that will return a list of PointT objects that represent some points on the borders of the region.
	 * 
	 * @return a list of PointT objects that represent some points on the borders of the region.
	 * @throws InvalidPointException If the value of x-coordinate is equal to or bigger than Constants.MAX_X this exception will be thrown. It will also throw this exception
	 * if the value of y-coordinate is equal to or bigger than Constants.MAX_Y.
	 */
	private PointT[] Region() throws InvalidPointException{
		int total_possibilities = (int) (2* (height+width));
		PointT[] q = new PointT[total_possibilities];
		
		int count = 0;
		
		/**The following for loops will make an array of the points that are there on the borders of the region. It will not have every single points on the borders.
		 * All the points will be 1 value away from each other. 
		 * 
		 */
		for (int i = 0 ; i < height ; i++){
			q[count] = new PointT(lower_left.xcrd() , lower_left.ycrd() + i);
			count++;
		}
		
		for (int i = 0; i < width; i++ ){
			q[count] = new PointT(lower_left.xcrd() + i , lower_left.ycrd());
			count++;
		}
		
		for (int i = 0; i < width; i++ ){
			q[count] = new PointT(lower_left.xcrd() + i , lower_left.ycrd() + height);
			count++;
		}
		
		for (int i = 0 ; i < height ; i++){
			q[count] = new PointT(lower_left.xcrd() + width , lower_left.ycrd() + i);
			count++;
		}
		
		return q;
	}
}
