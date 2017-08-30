package Assignment_3;
/**
 * <b> The purpose of this class is to generate an  exception, when it tries to add a point with invalid coordinates </b>
 * @author Amit Binu
 * @since 2017-03-20
 */
public class InvalidPointException extends Exception {
	/**
	 * This constructor creates the message that is to be displayed when this exception is caught. 
	 */
	public InvalidPointException(){
		super("This is an invalid point !!");
	}

}
