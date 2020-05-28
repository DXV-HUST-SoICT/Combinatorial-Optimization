package vuongdx.search.move;

import java.util.ArrayList;
import java.util.HashMap;

import localsearch.model.IConstraint;
import localsearch.model.IFunction;
import localsearch.model.VarIntLS;
import vuongdx.search.IMoveLS;

public class SingleVarChangeValue implements IMoveLS {
	
	private VarIntLS var;
	private int val;
	
	public SingleVarChangeValue() {
		
	}
	
	public SingleVarChangeValue(VarIntLS var, int val) {
		this.var = var;
		this.val = val;
	}

	public int movePropagate(HashMap<String, VarIntLS[]> dVar) {
		try {
			this.var.setValuePropagate(this.val);
			return 0;
		} catch (Exception e) {
			throw e;
		}
	}
	
	public int getMoveDelta(IFunction f, HashMap<String, VarIntLS[]> dVar) {
		try {
			int delta = f.getAssignDelta(this.var, this.val);
			return delta;
		} catch (Exception e) {
			throw e;
		}
	}

	public IMoveLS[] listMove(IFunction f, HashMap<String, VarIntLS[]> dVar) {
		ArrayList<SingleVarChangeValue> tmpMoveList = new ArrayList<SingleVarChangeValue>();
		for (String key : dVar.keySet()) {
			VarIntLS[] mVar = dVar.get(key);
			for (int i = 0; i < mVar.length; i++) {
				VarIntLS var = mVar[i];
				for (int val = var.getMinValue(); val <= var.getMaxValue(); val++) {
					tmpMoveList.add(new SingleVarChangeValue(var, val));
				}
			}
		}
		SingleVarChangeValue[] moveList = tmpMoveList.toArray(new SingleVarChangeValue[0]);
		return moveList;
	}
	
	public VarIntLS getVar() {
		return this.var;
	}
	
	public int getVal() {
		return this.val;
	}
	
	public boolean equals(SingleVarChangeValue other) {
		if (!this.getVar().equals(other.getVar())) {
			return false;
		}
		if (this.getVal() != other.getVal()) {
			return false;
		}
		return true;
	}
	
	public int hashCode() {
		Integer hc = this.var.hashCode();
		hc = hc * 31 + this.val;
		return hc;
	}
}
