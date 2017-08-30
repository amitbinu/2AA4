package Assignment_3;
/**
 * <b> The purpose of this class is to generate an  exception, when it tries to add a region whose corner's coordinates are biger than Constansts.MAX_X or / and Constants.MAX_Y</b>
 * @author Amit Binu
 * @since 2017-03-20
 */
public class InvalidRegionException extends Exception{

	/**
	 * This constructor creates the message that is to be displayed when this exception is caught. 
	 */
	public InvalidRegionException(){
		super("This is an invalid region!");
	}
}
