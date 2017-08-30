package Assignment_3;

/**
 * <b> The purpose of this class is to generate an  exception, when it tries to add a value into an already full GenreicList </b>
 * @author Amit Binu
 * @since 2017-03-20
 */
public class Map {
	/**
	 * This variable represents a GenreicList that will have regions of the obstacles that the robot might face.
	 */
public static Obstacles obstacles = new Obstacles();
/**
 * This variable represents a GenreicList that will have points of the destinations that the robot will have.
 */
public static Destinations destinations = new Destinations();
/**
 * This variable represents a GenericList that will have regions of the safezones in the robot's path.
 */
public static SafeZone safeZone = new SafeZone();

/**This method will transit the values of its parameters to the appropriate state variables.
 * 
 * @param o represents a GenreicList that will have regions of the obstacles that the robot might face.
 * @param d represents a GenreicList that will have points of the destinations that the robot will have.
 * @param sz represents a GenericList that will have regions of the safezones in the robot's path.
 */
public static void init(Obstacles o, Destinations d, SafeZone sz){
	obstacles = o;
	destinations = d;
	safeZone = sz;
}

/**This method returns the GenreicList that will have regions of the obstacles that the robot might face.
 * 
 * @return the GenreicList that will have regions of the obstacles that the robot might face.
 */
public static Obstacles get_obstacles(){
	return obstacles;
}

/**This method returns a GenreicList that will have points of the destinations that the robot will have.
 * 
 * @return a GenreicList that will have points of the destinations that the robot will have.
 */
public static Destinations get_destinations(){
	return destinations;
}

/**This method returns a GenericList that will have regions of the safezones in the robot's path.
 * 
 * @return a GenericList that will have regions of the safezones in the robot's path.
 */
public static SafeZone get_safeZone(){
	return safeZone;
}

}
