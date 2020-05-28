package vuongdx.search.legal;

import java.util.ArrayList;
import java.util.HashMap;

import localsearch.model.IFunction;
import localsearch.model.VarIntLS;
import vuongdx.search.ILegalMoveLS;
import vuongdx.search.IMemoryLS;
import vuongdx.search.IMoveLS;

public class TabuSTMMove implements ILegalMoveLS {
	
	private IMemoryLS mem;
	
	public TabuSTMMove(IMemoryLS mem) {
		this.mem = mem;
	}

	@Override
	public IMoveLS[] listLegal(IFunction f, HashMap<String, VarIntLS[]> dVar, IMoveLS[] moveList) {
		ArrayList<IMoveLS> tmpLegalMoveList = new ArrayList<IMoveLS>();
		Integer minDelta = Integer.MAX_VALUE;
		for (int i = 0; i < moveList.length; i++) {
			IMoveLS tmpMove = moveList[i];
			int delta = tmpMove.getMoveDelta(f, dVar);
			if (!(this.mem.inMemory(tmpMove)) || delta + f.getValue() < this.mem.getBestValue(f)) {
				if (delta <= minDelta) {
					if (delta < minDelta) {
						minDelta = delta;
						tmpLegalMoveList.clear();
					}
					tmpLegalMoveList.add(tmpMove);
				}
			}
		}
		IMoveLS[] legalMoveList = tmpLegalMoveList.toArray(new IMoveLS[0]);
		return legalMoveList;
	}
	
	public IMemoryLS getMem() {
		return mem;
	}

	public void setMem(IMemoryLS mem) {
		this.mem = mem;
	}

}
