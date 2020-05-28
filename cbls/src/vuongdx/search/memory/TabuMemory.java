package vuongdx.search.memory;

import java.util.HashMap;

import localsearch.model.IConstraint;
import localsearch.model.IFunction;
import vuongdx.search.IMemoryLS;
import vuongdx.search.IMoveLS;
import vuongdx.search.ISolutionLS;

public class TabuMemory extends MemoryLS implements IMemoryLS {
	
	public TabuMemory(Integer term) {
		this.move = new HashMap<>();
		this.solution = new HashMap<>();
		this.value = new HashMap<>();
		this.term = term;
		this.it = 0;
	}

	@Override
	public void rememberMove(IMoveLS m) {
		this.move.put(m, this.it + this.term);
		this.it += 1;
	}

	@Override
	public void rememberSolution(ISolutionLS s) {
		// TODO Auto-generated method stub

	}

	@Override
	public boolean inMemory(IMoveLS m) {
		if (!this.move.containsValue(m)) {
			return false;
		}
		if (this.move.get(m) <= this.it) {
			return false;
		}
		return true;
	}

	@Override
	public boolean inMemory(ISolutionLS s) {
		// TODO Auto-generated method stub
		return false;
	}

}
