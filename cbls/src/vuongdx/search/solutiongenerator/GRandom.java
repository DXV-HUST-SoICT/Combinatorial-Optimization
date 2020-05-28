package vuongdx.search.solutiongenerator;

import java.util.HashMap;
import java.util.Random;

import localsearch.model.VarIntLS;
import vuongdx.search.ISolutionGeneratorLS;

public class GRandom implements ISolutionGeneratorLS {

	@Override
	public void generateSolution(HashMap<String, VarIntLS[]> dVar) {
		Random r = new Random();
		for (String key : dVar.keySet()) {
			VarIntLS[] mVar = dVar.get(key);
			for (int i = 0; i < mVar.length; i++) {
				int v = r.nextInt(mVar[i].getMaxValue() - mVar[i].getMinValue() + 1) + mVar[i].getMinValue();
				mVar[i].setValuePropagate(v);
			}
		}
	}

}
