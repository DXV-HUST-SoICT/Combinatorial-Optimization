package vuongdx.search.move;

import java.util.ArrayList;
import java.util.HashMap;

import localsearch.model.IConstraint;
import localsearch.model.IFunction;
import localsearch.model.VarIntLS;
import vuongdx.search.IMoveLS;

public class ThreeVarSwap implements IMoveLS {
	
	private VarIntLS var1;
	private VarIntLS var2;
	private VarIntLS var3;
	
	public ThreeVarSwap() {
		
	}
	
	public ThreeVarSwap(VarIntLS var1, VarIntLS var2, VarIntLS var3) {
		this.var1 = var1;
		this.var2 = var2;
		this.var3 = var3;
	}

	@Override
	public int movePropagate(HashMap<String, VarIntLS[]> dVar) {
		try {
			int val1 = this.var1.getValue();
			int val2 = this.var2.getValue();
			int val3 = this.var3.getValue();
			this.var1.setValuePropagate(val2);
			this.var2.setValuePropagate(val3);
			this.var3.setValuePropagate(val1);
			return 0;
		} catch (Exception e) {
			throw e;
		}
	}

	@Override
	public int getMoveDelta(IFunction f, HashMap<String, VarIntLS[]> dVar) {
		try {
			int val1 = this.var1.getValue();
			int val2 = this.var2.getValue();
			int val3 = this.var3.getValue();
			this.var1.setValuePropagate(val2);
			this.var2.setValuePropagate(val3);
			this.var3.setValuePropagate(val1);
			int tmpValue = f.getValue();
			this.var1.setValuePropagate(val1);
			this.var2.setValuePropagate(val2);
			this.var3.setValuePropagate(val3);
			int delta = tmpValue - f.getValue();
			return delta;
		} catch (Exception e) {
			throw e;
		}
	}

	@Override
	public IMoveLS[] listMove(IFunction f, HashMap<String, VarIntLS[]> dVar) {
		ArrayList<ThreeVarSwap> tmpMoveList = new ArrayList<ThreeVarSwap>();
		for (String key : dVar.keySet()) {
			VarIntLS[] mVar = dVar.get(key);
			for (int i = 0; i < mVar.length; i++) {
				for (int j = i + 1; j < mVar.length; j++) {
					for (int k = i + 1; k < mVar.length; k++) {
						if (j != k) {
							tmpMoveList.add(new ThreeVarSwap(mVar[i], mVar[j], mVar[k]));
						}
					}
				}
			}
		}
		ThreeVarSwap[] moveList = tmpMoveList.toArray(new ThreeVarSwap[0]);
		return moveList;
	}

}
