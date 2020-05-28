package vuongdx.search;

import localsearch.model.ConstraintSystem;
import localsearch.model.LocalSearchManager;
import vuongdx.constraint.ConstraintSystemFunction;

public class AbstractSolver {
    protected LocalSearchManager lsm;
    protected ConstraintSystemFunction cs;
//    protected ConstraintSystem s;

    public AbstractSolver() {
        lsm = new LocalSearchManager();
//        s = new ConstraintSystem(lsm);
//        cs = new ConstraintSystemFunction(s);
        cs = new ConstraintSystemFunction(lsm);
    }
}
