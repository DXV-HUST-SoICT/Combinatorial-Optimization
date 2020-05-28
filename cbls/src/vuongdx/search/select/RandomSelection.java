package vuongdx.search.select;

import java.util.HashMap;
import java.util.Random;

import localsearch.model.IFunction;
import localsearch.model.VarIntLS;
import vuongdx.search.IMoveLS;
import vuongdx.search.ISelectMoveLS;

public class RandomSelection implements ISelectMoveLS {

	public IMoveLS select(IFunction f,
                          HashMap<String, VarIntLS[]> dVar,
                          IMoveLS[] moveList,
                          IMoveLS[] legalMoveList) {
		Random r = new Random();
		int idx = r.nextInt(legalMoveList.length);
		return legalMoveList[idx];
	}

}
