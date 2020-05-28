package coloring;

import localsearch.model.IConstraint;
import localsearch.model.LocalSearchManager;
import localsearch.model.VarIntLS;

import java.util.ArrayList;
import java.util.HashMap;

public class ColoringConstraint implements IConstraint {

    LocalSearchManager lsm;
    private int n;
    private ArrayList<Integer>[] edge;
    private int noViolation;
    private int[] varViolation;
    HashMap<VarIntLS, Integer> varMap;
    VarIntLS[] var;

    public ColoringConstraint(int n, ArrayList<Integer>[] edge, VarIntLS[] var) {
        this.n = n;
        this.edge = edge;
        this.var = var;
        this.varMap = new HashMap<>();
        for (int i = 0; i < var.length; i++) {
            this.varMap.put(var[i], i);
        }
        this.lsm = var[0].getLocalSearchManager();
    }

    @Override
    public int violations() {
        return this.noViolation;
    }

    @Override
    public int violations(VarIntLS x) {
        return varViolation[varMap.get(x)];
    }

    @Override
    public int getAssignDelta(VarIntLS x, int val) {
        int oldVal = x.getValue();
        if (oldVal == val) {
            return 0;
        }
        int res = 0;
        int idx = varMap.get(x);
        for (int i = 0; i < edge[idx].size(); i++) {
            if (var[edge[idx].get(i)].getValue() == oldVal) {
                res -= 2;
            }
            if (var[edge[idx].get(i)].getValue() == val) {
                res += 2;
            }
        }
        return res;
    }

    @Override
    public int getSwapDelta(VarIntLS x, VarIntLS y) {

        int xVal = x.getValue();
        int yVal = y.getValue();

        if (xVal == yVal) {
            return 0;
        }

        int res = 0;

        int idx = varMap.get(x);
        for (int i = 0; i < edge[idx].size(); i++) {
            if (var[edge[idx].get(i)].getValue() == xVal) {
                res -= 2;
            }

            if (var[edge[idx].get(i)].getValue() == yVal) {
                res += 2;
            }
        }

        idx = varMap.get(y);
        for (int i = 0; i < edge[idx].size(); i++) {
            if (var[edge[idx].get(i)].getValue() == yVal) {
                res -= 2;
            }

            if (var[edge[idx].get(i)].getValue() == xVal) {
                res += 2;
            }
        }

        return 0;
    }

    @Override
    public VarIntLS[] getVariables() {
        return this.var;
    }

    @Override
    public void propagateInt(VarIntLS x, int val) {
        if (!varMap.containsKey(x)) {
            return;
        }
        int idx = varMap.get(x);
        int oldVal = x.getOldValue();
        for (int i = 0; i < edge[idx].size(); i++) {
            if (var[edge[idx].get(i)].getValue() == oldVal) {
                noViolation -= 2;
                varViolation[idx] -= 1;
                varViolation[edge[idx].get(i)] -= 1;
            }

            if (var[edge[idx].get(i)].getValue() == val) {
                noViolation += 2;
                varViolation[idx] += 1;
                varViolation[edge[idx].get(i)] += 1;
            }
        }
    }

    @Override
    public void initPropagate() {
        this.noViolation = 0;
        for (int i = 0; i < n; i++) {
            this.varViolation[i] = 0;
            for (int j = 0; j < edge[i].size(); j++) {
                if (var[i].getValue() == var[edge[i].get(j)].getValue()) {
                    noViolation++;
                    varViolation[i]++;
                }
            }
        }
    }

    @Override
    public LocalSearchManager getLocalSearchManager() {
        return lsm;
    }

    @Override
    public boolean verify() {
        return (noViolation == 0);
    }
}
