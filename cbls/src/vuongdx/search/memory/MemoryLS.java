package vuongdx.search.memory;

import java.util.HashMap;

import localsearch.model.IConstraint;
import localsearch.model.IFunction;
import vuongdx.search.IMemoryLS;
import vuongdx.search.IMoveLS;
import vuongdx.search.ISolutionLS;

public class MemoryLS implements IMemoryLS {
	protected HashMap<IMoveLS, Integer> move;
	protected HashMap<ISolutionLS, Integer> solution;
	protected HashMap<IFunction, Integer> value;
	protected Integer term;
	protected Integer it;

	public MemoryLS() {
		move = new HashMap<>();
		solution = new HashMap<>();
		value = new HashMap<>();
		term = 0;
		it = 100;
	}

	@Override
	public void rememberMove(IMoveLS m) {

	}

	@Override
	public void rememberSolution(ISolutionLS s) {

	}

	@Override
	public boolean inMemory(IMoveLS m) {
		return false;
	}

	@Override
	public boolean inMemory(ISolutionLS s) {
		return false;
	}

	@Override
	public void rememberBestValue(IFunction f, Integer v) {
		if (value.get(f) != null) {
			value.put(f, Math.min(v, value.get(f)));
		} else {
			value.put(f, v);
		}
	}


	@Override
	public Integer getBestValue(IFunction f) {
		return value.get(f);
	}

}
