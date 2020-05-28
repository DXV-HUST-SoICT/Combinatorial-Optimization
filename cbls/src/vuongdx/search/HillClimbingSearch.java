package vuongdx.search;

import vuongdx.search.legal.BestMove;
import vuongdx.search.select.RandomSelection;

import java.util.HashMap;

import localsearch.model.IFunction;
import localsearch.model.VarIntLS;
;

public final class HillClimbingSearch extends LocalSearch {
	public HillClimbingSearch(IFunction f,
							  HashMap<String, VarIntLS[]> dVar,
							  IMoveLS moveRule) {
		super(f, dVar, moveRule, new BestMove(), new RandomSelection());
	}
}
