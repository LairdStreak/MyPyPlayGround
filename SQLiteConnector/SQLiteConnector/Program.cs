using System;
using System.Data.SQLite;

namespace SQLiteConnector
{
    class Program
    {

        private static string connectionString = @"Data Source=E:\Laird\GHUB\MyPyPlayGround\iotdata.db; Version=3; FailIfMissing=True; Foreign Keys=True;";
        static void Main(string[] args)
        {
            Add_Row();
            Read_Row();

            Console.WriteLine("Hello World!");
        }


        static void Read_Row()
        {
            using (SQLiteConnection conn = new SQLiteConnection(connectionString))
            {
                conn.Open();
                string sql = "SELECT top 10 * FROM dht11;";
                using (SQLiteCommand cmd = new SQLiteCommand(sql, conn))
                {
                    using (SQLiteDataReader reader = cmd.ExecuteReader())
                    {
                        while (reader.Read())
                        {
                            var temp = Int32.Parse(reader["temp"].ToString());
                            Console.WriteLine(temp);
                        }
                    }
                }
                conn.Close();
            }
        }


        static void Add_Row()
        {
            using (SQLiteConnection conn = new SQLiteConnection(connectionString))
            {
                conn.Open();
                using (SQLiteCommand cmd = new SQLiteCommand(conn))
                {
                    cmd.CommandText = "INSERT INTO dht11(temp,humidity,timestamp) VALUES (@temp,@humidity,@timestamp)";
                    cmd.Prepare();
                    cmd.Parameters.AddWithValue("@temp", 22);
                    cmd.Parameters.AddWithValue("@humidity", 55.3);
                    cmd.Parameters.AddWithValue("@timestamp", DateTime.Now.ToString());
                    try
                    {
                        var result = cmd.ExecuteNonQuery();
                    }
                    catch (SQLiteException e)
                    {
                        Console.WriteLine(e.Message);
                    }
                }
                conn.Close();
            }
        }
    }
}
