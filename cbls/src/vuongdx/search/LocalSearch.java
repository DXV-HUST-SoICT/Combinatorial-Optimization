package vuongdx.search;

import java.util.HashMap;

import localsearch.model.IFunction;
import localsearch.model.VarIntLS;

public class LocalSearch {
	public IFunction f;
	public HashMap<String, VarIntLS[]> dVar;
	public IMoveLS moveRule;
	public ILegalMoveLS legalMoveRule;
	public ISelectMoveLS selectMoveRule;
	
	public LocalSearch() {
		
	}
	
	public LocalSearch(IFunction f,
					   HashMap<String, VarIntLS[]> dVar,
					   IMoveLS moveRule,
					   ILegalMoveLS legalMoveRule,
					   ISelectMoveLS selectMoveRule) {
		this.f = f;
		this.dVar = dVar;
		this.moveRule = moveRule;
		this.legalMoveRule = legalMoveRule;
		this.selectMoveRule = selectMoveRule;
	}
	
	public int search() {
		IMoveLS[] moveList = this.moveRule.listMove(f, dVar);
		IMoveLS[] legalMoveList = this.legalMoveRule.listLegal(f, dVar, moveList);
		IMoveLS selectedMove = this.selectMoveRule.select(f, dVar, moveList, legalMoveList);
		selectedMove.movePropagate(dVar);
		return f.getValue();
	}
	
	public int search(int numIter) {
		int it = 0;
		while (f.getValue() > 0 && it < numIter) {
			it++;
			this.search();
		}
		return f.getValue();
	}
}
