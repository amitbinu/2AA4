package Assignment_3;
/**
 * <b> This class contains a GenereicList that has regions of the robot's obstacles in its path.  </b>
 * @author Amit Binu
 * @since 2017-03-20
 */
public class Obstacles extends GenericList {

	public GenericList<RegionT> OBSTACLES;
	
	/**
	 * This constructor will initialize a GenericList of regions and assigns it to the variable OBSTACLES.
	 */
	public Obstacles(){
		OBSTACLES = new GenericList<RegionT>();
	}
}
