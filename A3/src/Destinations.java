package Assignment_3;
/**
 * <b> This class contains a GenereicList that has points of the robot's destinations. </b>
 * @author Amit Binu
 * @since 2017-03-20
 */
public class Destinations extends GenericList{

	public GenericList<RegionT> DESTINATIONS;
	/**
	 * The constructor <b> Destinations() </b> initializes the GenericList <b> DESTINATIONS </b> which will have all the points of robot's destinations.
	 */
	public Destinations(){
		DESTINATIONS = new GenericList<RegionT>(); 
	}
}
