package vuongdx.setcover;

import localsearch.constraints.basic.LessThan;
import localsearch.functions.sum.SumFun;
import localsearch.functions.sum.SumVar;
import localsearch.model.ConstraintSystem;
import localsearch.model.IFunction;
import localsearch.model.LocalSearchManager;
import localsearch.model.VarIntLS;
import vuongdx.search.ISolver;

import java.io.FileInputStream;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.Scanner;

public class SetCover implements ISolver {

    private int n;
    private int m;
    private HashSet<Integer>[] contain;
    private HashSet<Integer>[] in;

    LocalSearchManager lsm = new LocalSearchManager();
    ConstraintSystem cs = new ConstraintSystem(lsm);
    VarIntLS[] x;

    @Override
    public void stateModel() {
        x = new VarIntLS[m];
        for (int i = 0; i < m; i++) {
            x[i] = new VarIntLS(lsm, -1, 0);
        }
        IFunction count = new SumVar(x);
        for (int i = 0; i < n; i++) {
            ArrayList<VarIntLS> tmp = new ArrayList<>();
            for (Integer j : in[i]) {
                tmp.add(x[j]);
            }
            VarIntLS[] tmp2 = tmp.toArray(new VarIntLS[0]);
            IFunction tmpC = new SumVar(tmp2);
//            cs.post(new LessThan(tmpC, 0));
        }
    }

    @Override
    public void search() {

    }

    @Override
    public void printResult() {

    }

    public static void main(String[] args) {
        SetCover sc = new SetCover("./data/setcover/sc_6_1");
    }

    public void readInput(String file) {
        try {
            FileInputStream fis = new FileInputStream(file);
            Scanner s = new Scanner(fis);
            this.n = s.nextInt();
            this.m = s.nextInt();
            contain = new HashSet[m];
            in = new HashSet[n];
            for (int i = 0; i < m; i++) {
                String[] line = s.nextLine().split(" ");
                for (int j = 0; j < line.length; j++) {
                    int v = Integer.parseInt(line[i]);
                    contain[i].add(v);
                    in[v].add(i);
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public SetCover(String file) {
        this.readInput(file);
    }
}
