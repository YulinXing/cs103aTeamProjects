/*
  transaction.js -- Router for the showTransaction
*/
const express = require('express');
const router = express.Router();
const ToDoItem = require('../models/ToDoItem')
const Transaction = require('../models/Transaction')
const User = require('../models/User')
const moment = require('moment-timezone');


/*
this is a very simple server which maintains a key/value
store using an object where the keys and values are lists of strings

*/

isLoggedIn = (req,res,next) => {
  if (res.locals.loggedIn) {
    next()
  } else {
    res.redirect('/login')
  }
}


router.get('/transaction/',
  isLoggedIn,
  async (req, res, next) => {
    const show = req.query.show;
    const records = await Transaction.find().lean();
    for (let i = 0; i < records.length; i++) {
      const record = records[i];
      record.dateFormatted = moment(record.date).tz('America/New_York').format('ddd MMM DD YYYY');
    }
    res.render('showTransaction', {records, show});
});


router.get('/sortBy/', isLoggedIn, async (req, res, next) => {
  const show = req.query.show;
  let records = [];
  if (show === 'sortByCategory') {
    records = await Transaction.find().sort({ category: 1 }).lean();
    for (let i = 0; i < records.length; i++) {
      const record = records[i];
      record.dateFormatted = moment(record.date).tz('America/New_York').format('ddd MMM DD YYYY');
    }
  } else if (show === 'sortByAmount') {
    records = await Transaction.find().sort({ amount: 1 }).lean();
    for (let i = 0; i < records.length; i++) {
      const record = records[i];
      record.dateFormatted = moment(record.date).tz('America/New_York').format('ddd MMM DD YYYY');
    }
  } else if (show === 'sortByDescription') {
    records = await Transaction.find().sort({ description: 1 }).lean();
    for (let i = 0; i < records.length; i++) {
      const record = records[i];
      record.dateFormatted = moment(record.date).tz('America/New_York').format('ddd MMM DD YYYY');
    }
  } else if (show === 'sortByDate') {
    records = await Transaction.find().lean();
    for (let record of records) {
      record.dateFormatted = moment(record.date || record.createdAt).tz('America/New_York').format('ddd MMM DD YYYY');
    }
    records.sort((a, b) => moment(a.date || a.createdAt).diff(moment(b.date || b.createdAt)));
  }
  
  res.render('showTransaction', { records, show });
});


/* add the value in the body to the list associated to the key */
router.post('/transaction',
  isLoggedIn,
  async (req, res, next) => {
      const createdAt = moment(req.body.createdAt).tz('America/New_York').format('ddd MMM DD YYYY');
      const transaction = new Transaction(
        {
          description: req.body.description,
          amount: req.body.amount,
          category: req.body.category,
          createdAt: new Date(createdAt),
          userId: req.user._id
        })
      await transaction.save();
      res.redirect('/transaction')
});


router.get('/transaction/remove/:itemId',
  isLoggedIn,
  async (req, res, next) => {
      console.log("inside /transaction/remove/:itemId")
      await Transaction.deleteOne({_id:req.params.itemId});
      res.redirect('/transaction')
});


router.get('/transaction/edit/:itemId',
  isLoggedIn,
  async (req, res, next) => {
      console.log("inside /transaction/edit/:itemId")
      const item = 
       await Transaction.findById(req.params.itemId);
      //res.render('edit', { item });
      res.locals.item = item
      res.render('editTransaction')
      //res.json(item)
});


router.post('/transaction/updateTransaction/:itemId',
  isLoggedIn,
  async (req, res, next) => {
      const {itemId,description,amount,category,createdAt} = req.body;
      console.log("inside /transaction/updateTransaction/:itemId");
      await Transaction.findOneAndUpdate(
        {_id:itemId},
        {$set: {description,amount,category,createdAt}} );
      res.redirect('/transaction')
});


router.get('/transaction/byCategory',
  isLoggedIn,
  async (req, res, next) => {
    let results = 
          await Transaction.aggregate(
            [
              {$group: {
                _id: '$category',
                total: { $sum: '$amount' }
                }},
              {$sort: {total: -1,}},
            ])
 
      res.render('summarizeByCategory', { results });
});


module.exports = router;
