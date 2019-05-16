package com.kejing.test

import org.apache.spark.rdd.RDD
import org.apache.spark.sql.Row
import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.types._
import org.apache.spark.sql.DataFrame

/**
 * java.lang.ArrayIndexOutOfBoundsException: 10582
 * 二次排序的几种解决办法
 */

object TwiceOrder {
  
  def main(args:Array[String]){
    
      val spark = SparkSession.builder.appName("abc").master("local").getOrCreate()
      
      val schema = StructType(List(
        StructField("year", IntegerType, nullable = true),
        StructField("month", IntegerType, nullable = true)
      ))
      
      val data = Array(
        Row(2014,3),
        Row(2014,1),
        Row(2012,6),
        Row(2012,2),
        Row(2012,4),
        Row(2017,8),
        Row(2018,9),
        Row(2018,5)
      )
      
      val rdd:RDD[Row] = spark.sparkContext.parallelize(data)
      
      val df:DataFrame =  spark.createDataFrame(rdd, schema)
      
      df.printSchema()
      
      val r2 = df.rdd
      r2.cache()
      
      /**** 第一种实现方式: 采用dataFrame，直接使用sort就可以实现二次排序  ****/
      val r = df.sort("year", "month")
      r.show(false)
      println("---------------r1")
      
      /**** 第二种方式：使用class继承Ordered类，重写compare方法来实现二次排序。 ****/
      val pr3:RDD[Cont] = r2.map(row =>new Cont(row.getAs[Int]("year"),row.getAs[Int]("month")))
      val r3 = pr3.sortBy(t => t)
      r3.foreach(println)
      println("---------------r2")
      
      /**** 第三种方式：使用继承了Ordered类的来实现二次排序(下面三种隐式方式都可用)   ****/
      val pr4:RDD[(Int,Int)] = r2.map(row => (row.getAs[Int]("year"), row.getAs[Int]("month")))
      
      implicit def ordMethod(cont:Cont2):Ordered[Cont2] = new Ordered[Cont2]{
        override def compare(thatCont:Cont2):Int = {
          if(cont.year == thatCont.year){
            cont.month - thatCont.month
          }else{
            cont.year - thatCont.year
          }
        }
      }
      implicit def ordFunc = (cont:Cont2) => new Ordered[Cont2]{
        override def compare(thatCont:Cont2):Int = {
          if(cont.year == thatCont.year){
            cont.month - thatCont.month
          }else{
            cont.year - thatCont.year
          }
        }
      }
      implicit object ord extends Ordering[Cont2]{
        override def compare(x:Cont2, y:Cont2):Int = {
          if(x.year == y.year){
            x.month - y.month
          }else{
            x.year - y.year
          }
        }
      }
      val r4 = pr4.sortBy(t => new Cont2(t._1, t._2))
      r4.foreach(println)
      println("---------------r3")
      
      /**** 第四种范式：直接使用元组封装排序条件  ****/ 
      val r5 = pr4.sortBy(t => (t._1, t._2))
      r5.foreach(println)
      println("---------------r4")
      
  }
  
}

class Cont(val year:Int, val month:Int) extends Serializable with Ordered[Cont]{
  
    override def compare(that: Cont):Int = {
      //根据year值排序，如果相同，再按照月份排序
      if(this.year == that.year){
        this.month - that.month
      }else{
        this.year - that.year
      }
    }
    
    override def toString():String = {
      s"year:${this.year}, month:${this.month}"
    }
    
}
  
class Cont2(val year:Int, val month:Int) extends Serializable{
    
    override def toString():String = {
      s"year:${this.year}, month:${this.month}"
    }
}


