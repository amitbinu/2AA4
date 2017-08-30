package Assignment_3;
/**
 * <b> The purpose of this class is to generate an  exception, when it tries to add something to the GenericList at an invalid position </b>
 * @author Amit Binu
 * @since 2017-03-20
 */
public class InvalidPositionException extends Exception{
	/**
	 * This constructor creates the message that is to be displayed when this exception is caught. 
	 */
	public InvalidPositionException(){
		super("The given position is invalid !!");
	}

}
