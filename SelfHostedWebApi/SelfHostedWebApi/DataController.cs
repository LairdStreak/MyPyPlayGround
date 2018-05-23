using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Web.Http;
using System.Web.Mvc;

namespace SelfHostedWebApi
{
    public class DataController : ApiController
    {
        [System.Web.Http.HttpGet]
        public ActionResult Index()
        {
            return new HttpStatusCodeResult(200);
        }

        //[System.Web.Http.HttpGet]
        //public ActionResult Index(string id)
        //{
        //    return new HttpStatusCodeResult(200);
        //}

        [System.Web.Http.HttpPost]
        public ActionResult Index([FromBody] dynamic jsonBody)
        {
            Console.WriteLine(jsonBody);
            return new HttpStatusCodeResult(200);
        }
    }
}
