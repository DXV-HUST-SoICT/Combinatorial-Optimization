package vuongdx.search;

import localsearch.model.LocalSearchManager;
import vuongdx.constraint.ConstraintSystemFunction;

public interface ISolver {
	
	public void stateModel();
	
	public void search();
	
	public void printResult();

}
