package vuongdx.search;

import java.util.HashMap;

import localsearch.model.IFunction;
import localsearch.model.VarIntLS;

public interface IMoveLS {

	public int movePropagate(HashMap<String, VarIntLS[]> dVar);
	
	public int getMoveDelta(IFunction f, HashMap<String, VarIntLS[]> dVar);
	
	public IMoveLS[] listMove(IFunction f,
							  HashMap<String, VarIntLS[]> dVar);

}