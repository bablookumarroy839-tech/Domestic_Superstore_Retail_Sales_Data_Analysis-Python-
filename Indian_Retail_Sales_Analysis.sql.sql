 create table indian_retail_store (
 bill_id int  primary key,
 customer_name varchar(50),
 city varchar(50),
 product_category varchar(50),
 quantity int,
 total_amount int,
 payment_method varchar(50),
 store_type varchar(50),
 visit_date int
 );
 
 alter table indian_retail_store 
 drop column visit_date;
 
 alter table indian_retail_store
alter column total_amount type numeric(10,2)

 select * from indian_retail_store;
 select sum(total_amount) from indian_retail_store;
 
 select product_category, sum(total_amount) as total
 from indian_retail_store
 group by product_category
 order by total desc;
 
 select product_category, sum(quantity) as total
 from indian_retail_store
 group by product_category
 order by total desc;
 
 select city, sum(total_amount) as total
 from indian_retail_store
 group by city
 order by total desc
 limit 10;
 
 
 select customer_name , sum(total_amount) as total from indian_retail_store 
 group by customer_name 
 order by total desc
 limit 10;

 
 select product_category , sum(total_amount) as total,
 rank() over(order by sum(total_amount)desc )
 from indian_retail_store
 group by product_category;
 
 
   

   