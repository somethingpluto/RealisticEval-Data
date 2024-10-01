  //Multi-filter based on an interface
  async function multiFilter(filterFormat: BuyOrderFilter) {
    // This AQL query is written by chatGPT
    const result = await MyDatabase.getDb().query(aql`
      FOR bo IN BuyOrders
      FILTER ${
        filterFormat.product_id
          ? aql`bo.product_id == ${filterFormat.product_id}`
          : aql`true`
      }
      FILTER ${
        filterFormat.supplier_id
          ? aql`bo.customer_id == ${filterFormat.supplier_id}`
          : aql`true`
      }
      FILTER ${
        filterFormat.amount_from
          ? aql`bo.amount >= ${filterFormat.amount_from}`
          : aql`true`
      }
      FILTER ${
        filterFormat.amount_to
          ? aql`bo.amount <= ${filterFormat.amount_to}`
          : aql`true`
      }
      FILTER ${
        filterFormat.status
          ? aql`bo.status == ${filterFormat.status}`
          : aql`true`
      }
      FILTER ${
        filterFormat.date_from
          ? aql`bo.date >= ${filterFormat.date_from}`
          : aql`true`
      }
      FILTER ${
        filterFormat.date_to
          ? aql`bo.date <= ${filterFormat.date_to}`
          : aql`true`
      }
      RETURN bo
    `);
    const finallyResult: BuyOrderEntity[] = await result.all();
    return finallyResult;
  }