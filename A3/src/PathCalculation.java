package Assignment_3;
/** <b> This class has methods that does some calculation using PathT objects. </b>
 * 
 * @author Amit Binu
 * @since 2017-03-20
 *
 */

public class PathCalculation {
	
	/** This method calculates the total distance of robot's path using the  <b> dist </b>  method in the <b>PointT </b> module 
	 * 
	 * @param p is a PathT object, which is a GenericList that contains points/coordinates of the robot's paths. 
	 * @return a double value that represents the total distance of robot's path.
	 * @throws InvalidPositionException if it tries to get a point in an invalid position in the path object.
	 */
	
	public static double totalDistance(PathT p) throws InvalidPositionException{
		double distance = 0;
		
		for (int i =0; i< p.size()-1; i++){
			PointT temp =  (PointT) p.getval(i);
			PointT temp1 = (PointT) p.getval(i+1);
			
			distance += temp.dist(temp1);
		}
		return distance;
	}
	
	/** This class calculates the total number of turns the robot made in its path. It uses the local function angle to calculate this. 
	 * 
	 * @param p is a PathT object, which is a GenericList that contains points/coordinates of the robot's paths. 
	 * @return a double value that represents the total number of turns the robot made in its path.
	 * @throws InvalidPositionException if it tries to get a point in an invalid position in the path object.
	 */
	public static double totalTurns(PathT p) throws InvalidPositionException{
		double turns = 0;
		for (int i =0; i < p.size() -2; i++){
			if (angle((PointT)p.getval(i), (PointT) p.getval(i+1), (PointT) p.getval(i+2) ) != 0)
				turns++;
		}
		return turns;
	}
	

	/**This class uses the local functions <b> linear_time </b> and <b> angular_time </b> to calculate and return the total time the robot took to finish its path.
	 * 
	 * @param p is a PathT object, which is a GenericList that contains points/coordinates of the robot's paths.
	 * @return a double value that represent the total time the robot took to finish its path.
	 * @throws InvalidPositionException if it tries to get a point in an invalid position in the path object.
	 */
	public static double estimatedTime(PathT p) throws InvalidPositionException{
		
		return linear_time(p) + angular_time(p);
	}
	
	/** This is a local function that takes 3 PointT objects and uses them to calculate the angle between the 3  points. 
	 * 
	 * @param p1 is a PointT object whose coordinates are used to calculate the angle between the 3  points.
	 * @param p2 is a PointT object whose coordinates are used to calculate the angle between the 3  points.
	 * @param p3 is a PointT object whose coordinates are used to calculate the angle between the 3  points.
	 * @return a double value that represents the angle between the line (p1,p2) and the line (p2,p3). 
	 */
	private static double angle(PointT p1, PointT p2, PointT p3){
		double numerator = (p2.xcrd() - p1.xcrd()) * (p3.xcrd() - p2.xcrd()) + (p2.ycrd() - p1.ycrd()) * (p3.ycrd() - p2.ycrd());
		double denominator = p1.dist(p2) * p2.dist(p3);
		return Math.acos(numerator / denominator );
	}

	/** This is a local function that takes a PathT object and uses them to calculate the linear time the robot took to move around its path. 
	 * 
	 * @param p is a GenericList of PathT which contains PointT object whose coordinates are used to calculate the linear_time.
	 * @return  a double value that represents the linear_time the robot took to move around its path.
	 * @throws InvalidPositionException
	 */
	private static double linear_time(PathT p) throws InvalidPositionException {
		// TODO Auto-generated method stub
		double time = 0;
		for (int i = 0; i< p.size() -1; i++){
			time += (((PointT) p.getval(i)).dist((PointT) p.getval(i+1))) /  (Constants.VELOCITY_LINEAR) ;
		}
		return time;
	}
	
	/**This is a local function that takes a PathT object and uses them to calculate the angular time the robot took to move around its path. 
	 * 
	 * @param p is a GenericList of PathT which contains PointT object whose coordinates are used to calculate the angular time..
	 * @return a double value that represents the angular time the robot took to move around its path.
	 * @throws InvalidPositionException
	 */
	private static double angular_time(PathT p) throws InvalidPositionException {
		// TODO Auto-generated method stub
		double time = 0;
		for (int i = 0; i< p.size() -1; i++){
			time += (((PointT) p.getval(i)).dist((PointT) p.getval(i+1))) /  (Constants.VELOCITY_ANGULAR) ;
		}
		return time;
	}

	

}
