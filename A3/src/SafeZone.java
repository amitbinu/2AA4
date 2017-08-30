package Assignment_3;
/**
 * <b> This class contains a GenereicList that has regions of the robot's obstacles in its path.  </b>
 * @author Amit Binu
 * @since 2017-03-20
 */
public class SafeZone extends GenericList{

	public GenericList<RegionT> SafeZone;
	
	/**
	 * 
	 */
	public SafeZone(){
		SafeZone = new GenericList<RegionT>();
		SafeZone.MAX_SIZE = 1;
	}
}
