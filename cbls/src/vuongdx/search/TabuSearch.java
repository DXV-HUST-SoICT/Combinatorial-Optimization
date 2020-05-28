package vuongdx.search;

import java.util.HashMap;

import localsearch.model.ConstraintSystem;
import localsearch.model.IFunction;
import localsearch.model.VarIntLS;
import vuongdx.search.legal.TabuSTMMove;
import vuongdx.search.memory.TabuMemory;
import vuongdx.search.select.RandomSTMSelection;

public class TabuSearch extends LocalSearch {
	private TabuMemory mem;
	
	public TabuSearch(IFunction f,
					  HashMap<String, VarIntLS[]> dVar,
					  IMoveLS moveRule, Integer term) {
		this.mem = new TabuMemory(term);
		this.f = f;
		this.dVar = dVar;
		this.moveRule = moveRule;
		this.legalMoveRule = new TabuSTMMove(this.mem);
		this.selectMoveRule = new RandomSTMSelection(this.mem);
	}
	
	public TabuSearch(IFunction f,
			HashMap<String, VarIntLS[]> dVar,
			IMoveLS moveRule) {
		this(f, dVar, moveRule, 0);
	}

	public int search(int numIter, int maxStable, ISolutionGeneratorLS g) {
		int it = 0;
		int nic = 0;
		this.mem.rememberBestValue(f, f.getValue());
		while (f.getValue() > 0 && it < numIter) {
			System.out.println("Iter " + it + ": " + f.getValue());
			it++;
			this.search();
			if (f.getValue() < this.mem.getBestValue(f)) {
				nic = 0;
				this.mem.rememberBestValue(f, f.getValue());
			} else {
				nic++;
				if (nic >= maxStable) {
					g.generateSolution(dVar);
				}
			}
		}
		return f.getValue();
	}
}
