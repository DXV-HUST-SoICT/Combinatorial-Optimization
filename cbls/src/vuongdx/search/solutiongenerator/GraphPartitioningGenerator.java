package vuongdx.search.solutiongenerator;

import java.util.HashMap;

import localsearch.model.VarIntLS;
import vuongdx.search.ISolutionGeneratorLS;

public class GraphPartitioningGenerator implements ISolutionGeneratorLS {

	@Override
	public void generateSolution(HashMap<String, VarIntLS[]> dVar) {
		for (String key : dVar.keySet()) {
			VarIntLS[] mVar = dVar.get(key);
			for (int i = 0; i < mVar.length / 2; i++) {
				mVar[i].setValuePropagate(0);
			}
			for (int i = mVar.length / 2; i < mVar.length; i++) {
				mVar[i].setValuePropagate(1);
			}
		}
	}

}
