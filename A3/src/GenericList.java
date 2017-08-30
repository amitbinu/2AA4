package Assignment_3;

import java.util.ArrayList;
/**<b> THis module/class will create a GenericList with ArrayList. This module will be used to generate list for PointT objects and RegionT objects.
 * 
 * @author Amit Binu
 * @since 2017 - -03- 20
 * @param <T> This will define what type of objects are added into the GenricList.
 */
public class GenericList<T> {
	
	private ArrayList<T> s; 
	/**
	 * This variable contains an integer value that represents the maximum size of the GenericList. 
	 */
	public static int MAX_SIZE = 100;
	
	/**
	 * This constructor will make an ArrayList and initializes the ArrayList<T> s. 
	 */
	public GenericList(){
		ArrayList<T> x1= new ArrayList<T>();
		
		this.s=x1;
		
	
	}

	/**This method is used to add objects into the GenricList
	 * 
	 * @param i is an integer value that represents the position where the value should be inserted in the GenericList. 
	 * @param p is an object of type T and is the value that will be added to the GenericLsit.
	 * @throws FullSequenceException when the GenericList's size is MAX_SIZE and when it tries to add a value to a new valid position, this exception will be thrown.
	 * @throws InvalidPositionException when an invalid i is used. So, for example if i was -1 then this exception will be thrown.
	 */
	public void add (int i, T p) throws FullSequenceException, InvalidPositionException{
		
		if (s.size() == MAX_SIZE)
			throw new FullSequenceException();
	
		if (i < 0 || i > s.size())
			throw new InvalidPositionException();
		
		s.add(i, p);
		
	}
	
	/**This method will delete / remove the position that is mentioned in its parameter.
	 * 
	 * @param i is an integer value that represent the position of a value in the GenericList.
	 * @throws InvalidPositionException when an invalid i  / non existing position is used, this exception is thrown. So, for example if i was -1 then this exception will be thrown.
	 */
	public void del(int i) throws InvalidPositionException{
		if (i < 0 || i > s.size() -1)
			throw new InvalidPositionException();
		s.remove(i);
	}
	
	/**This method will replace the value at the position i with a new value.
	 * 
	 * @param i is an integer value that represent the position of a value in the GenericList.
	 * @param p is an object of type T and is the new value that will replace the old value in the GenericLsit.
	 * @throws InvalidPositionException when an invalid i  / non existing position is used, this exception is thrown. So, for example if i was -1 then this exception will be thrown.
	 */
	public void setval(int i, T p) throws InvalidPositionException{
		if (i < 0 || i > s.size() -1)
			throw new InvalidPositionException();
		s.set(i, p);
	}
	
	/**This method will return the value at a certain position in the GenericList.
	 * 
	 * @param i is an integer value that represent the position of a value in the GenericList.
	 * @return an object of type T and is the value at the position <b> i </b> in the GenericLsit.
	 * @throws InvalidPositionException when an invalid i  / non existing position is used, this exception is thrown. So, for example if i was -1 then this exception will be thrown.
	 */
	public T getval(int i) throws InvalidPositionException{
		if (i < 0 || i > s.size() -1)
			throw new InvalidPositionException();
		return s.get(i);
	}
	
	/**THis method will return the size of the GenericList's size.
	 * 
	 * @return an integer value that represents the size of the GenricList.
	 */
	public int size(){
		return s.size();
	}
}
