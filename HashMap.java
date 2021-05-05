package com.company;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Main {

    public static void main(String[] args) {
	// write your code here
       // hashTable1();
        //hashTable2();
        hashTable3();
    }

    static void  hashTable1()
    {
        Map<Integer,String> hashTable1 = new HashMap<Integer,String>();
        hashTable1.put(1,"Phien");
        hashTable1.put(2,"Duc");
        hashTable1.put(3,"Tai");
        hashTable1.put(3,"Quang Anh");
        hashTable1.put(4,"Son");
        hashTable1.put(5,"Phong");
        for (Map.Entry m:hashTable1.entrySet()) {
            System.out.println(m.getKey()+" "+m.getValue());
        }

        //hashTable1.putAll();
        hashTable1.remove(1,"Phien");
        hashTable1.replace(3,"Quang Anh","Tai");

        System.out.printf("\n");
        for (Map.Entry m:hashTable1.entrySet()) {
            System.out.println(m.getKey()+" "+m.getValue());
        }
    }

    static void hashTable2()
    {
        Map<String,List> hashTable2 = new HashMap<String,List>();
        List<Integer> lst1 = new ArrayList<>();
        lst1.add(1);
        lst1.add(2);
        lst1.add(3);
        lst1.add(4);
        lst1.add(5);
        List<String> lst2 = new ArrayList<>();
        lst2.add("A");
        lst2.add("B");
        lst2.add("C");
        lst2.add("D");
        lst2.add("E");
        List<Float> lst3 = new ArrayList<>();
        lst3.add((float) 1.3);
        lst3.add((float) 1.4);
        lst3.add((float) 5.3);
        lst3.add((float) 7.3);
        lst3.add((float) 9.3);

        List lst4 = new ArrayList<Integer>();
        lst4.add("Mot");
        lst4.add(2);
        lst4.add(6);
        lst4.add(1.3);
        lst4.add(34);
        lst4.add("Nam");

        hashTable2.put("Phien",lst1);
        hashTable2.put("Phien",lst4);
        hashTable2.put("Dat",lst2);
        hashTable2.put("Phong",lst3);
        hashTable2.put("Son",lst1);
        for (Map.Entry item:hashTable2.entrySet())
        {
            String name = (String)item.getKey();
            List lst = (List)item.getValue();
            for (Object obj:lst) {
                System.out.println(name + " " + obj.toString());
            }
        }
    }

    static void hashTable3()
    {
        Map<List,List> hashTable3= new HashMap<>();
        List<Integer> lst1 = new ArrayList<>();
        lst1.add(1);
        lst1.add(2);
        lst1.add(3);
        lst1.add(4);
        lst1.add(5);
        List<String> lst2 = new ArrayList<>();
        lst2.add("A");
        lst2.add("B");
        lst2.add("C");
        lst2.add("D");
        lst2.add("E");
        List<Float> lst3 = new ArrayList<>();
        lst3.add((float) 1.3);
        lst3.add((float) 1.4);
        lst3.add((float) 5.3);
        lst3.add((float) 7.3);
        lst3.add((float) 9.3);

        List lst4 = new ArrayList<Integer>();
        lst4.add("Mot");
        lst4.add(2);
        lst4.add(6);
        lst4.add(1.3);
        lst4.add(34);
        lst4.add("Nam");

        hashTable3.put(lst1,lst2);
        hashTable3.put(lst1,lst3);
        hashTable3.put(lst2,lst1);
        hashTable3.put(lst3,lst4);
        hashTable3.put(lst4,lst1);

        for (Map.Entry item : hashTable3.entrySet())
        {
            List lstKey = (List) item.getKey();
            List lstValue = (List)item.getValue();

            for (Object obj : lstKey) {
                System.out.println(obj.toString());
            }

            for (Object obj : lstValue)
            {
                System.out.println(obj.toString());
            }
        }
    }
}
