

document.addEventListener("DOMContentLoaded", () => {
  document
      .querySelectorAll(
        "table:not(.card-body table):not(form table):not(.recommendation-card table)",
      )
      .forEach((table) => {
        try {
          const dbtable = new DataTable(table, {
            order: [],
          });
        } catch (error) {}
      });
  });