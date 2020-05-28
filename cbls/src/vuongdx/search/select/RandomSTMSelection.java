package vuongdx.search.select;

import java.util.HashMap;

import localsearch.model.IFunction;
import localsearch.model.VarIntLS;
import vuongdx.search.IMemoryLS;
import vuongdx.search.IMoveLS;
import vuongdx.search.ISelectMoveLS;

public class RandomSTMSelection extends RandomSelection implements ISelectMoveLS {
	
	IMemoryLS mem;
	
	public RandomSTMSelection(IMemoryLS mem) {
		this.mem = mem;
	}
	
	public IMoveLS select(IFunction f,
                          HashMap<String, VarIntLS[]> dVar,
                          IMoveLS[] moveList,
                          IMoveLS[] legalMoveList) {
		IMoveLS selectedMove = super.select(f, dVar, moveList, legalMoveList);
		this.mem.rememberMove(selectedMove);
		return selectedMove;
	}
	
	public IMemoryLS getMem() {
		return mem;
	}

	public void setMem(IMemoryLS mem) {
		this.mem = mem;
	}

}
