package vuongdx.search;

import localsearch.model.IConstraint;
import localsearch.model.IFunction;

public interface IMemoryLS {
	public void rememberMove(IMoveLS m);
	public boolean inMemory(IMoveLS m);
	public void rememberSolution(ISolutionLS s);
	public boolean inMemory(ISolutionLS s);
	public void rememberBestValue(IFunction f, Integer v);
	public Integer getBestValue(IFunction f);
}
