package Assignment_3;

/**
 * <b> This class contains a GenereicList that has points of the robot's path.  </b>
 * @author Amit Binu
 * @since 2017-03-20
 */
public class PathT extends GenericList{
	
	public GenericList<PointT> PATH; 
	
	/**
	 * This constructor will initialize a GenericList of points and assigns it to the variable PATH.
	 */
	public PathT(){
		PATH = new GenericList<PointT> ();
	}
	
}
