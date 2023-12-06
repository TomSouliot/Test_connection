
from google.cloud import bigquery

def subscriptions_schema():
    """
    This function defines the schema for the raw_subscriptions table.
    Args:
    Returns:
        A schema object that can be used for the bigquery client to create the table
    """
    table_schema_subscriptions = [
            bigquery.SchemaField("subscription__id", "STRING", mode="REQUIRED"),
            bigquery.SchemaField("subscription__billing_period", "INTEGER", mode="NULLABLE"),
            bigquery.SchemaField("subscription__billing_period_unit", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("subscription__auto_collection", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("subscription__customer_id", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("subscription__status", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("subscription__current_term_start", "TIMESTAMP", mode="NULLABLE"),
            bigquery.SchemaField("subscription__current_term_end", "TIMESTAMP", mode="NULLABLE"),
            bigquery.SchemaField("subscription__next_billing_at", "TIMESTAMP", mode="NULLABLE"),
            bigquery.SchemaField("subscription__created_at", "TIMESTAMP", mode="NULLABLE"),
            bigquery.SchemaField("subscription__started_at", "TIMESTAMP", mode="NULLABLE"),
            bigquery.SchemaField("subscription__activated_at", "TIMESTAMP", mode="NULLABLE"),
            bigquery.SchemaField("subscription__created_from_ip", "INTEGER", mode="NULLABLE"),
            bigquery.SchemaField("subscription__updated_at", "TIMESTAMP", mode="NULLABLE"), # checked
            bigquery.SchemaField("subscription__has_scheduled_changes", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("subscription__offline_payment_method", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("subscription__channel", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("subscription__resource_version", "INTEGER", mode="NULLABLE"),
            bigquery.SchemaField("subscription__deleted", "STRING", mode="NULLABLE"),# checked
            bigquery.SchemaField("subscription__object", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("subscription__coupon", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("subscription__currency_code", "STRING", mode="NULLABLE"),# checked
            bigquery.SchemaField("subscription__subscription_items", "JSON", mode="NULLABLE"),
            bigquery.SchemaField("subscription__item_tiers", "JSON", mode="NULLABLE"),# checked
            bigquery.SchemaField("subscription__coupons", "JSON", mode="NULLABLE"),
            bigquery.SchemaField("subscription__due_invoices_count", "INTEGER", mode="NULLABLE"),
            bigquery.SchemaField("subscription__due_since", "TIMESTAMP", mode="NULLABLE"),# checked
            bigquery.SchemaField("subscription__total_dues", "INTEGER", mode="NULLABLE"),
            bigquery.SchemaField("subscription__mrr", "INTEGER", mode="NULLABLE"),# checked
            bigquery.SchemaField("subscription__exchange_rate", "FLOAT", mode="NULLABLE"),
            bigquery.SchemaField("subscription__base_currency_code", "STRING", mode="NULLABLE"),# checked
            bigquery.SchemaField("subscription__has_scheduled_advance_invoices", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("subscription__create_pending_invoices", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("subscription__auto_close_invoices", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("customer__id", "STRING", mode="REQUIRED"),
            bigquery.SchemaField("customer__first_name", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("customer__last_name", "STRING", mode="NULLABLE"),# checked
            bigquery.SchemaField("customer__email", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("customer__company", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("customer__auto_collection", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("customer__offline_payment_method", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("customer__net_term_days", "INTEGER", mode="NULLABLE"),
            bigquery.SchemaField("customer__allow_direct_debit", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("customer__created_at", "TIMESTAMP", mode="NULLABLE"),
            bigquery.SchemaField("customer__created_from_ip", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("customer__taxability", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("customer__updated_at", "TIMESTAMP", mode="NULLABLE"),# checked
            bigquery.SchemaField("customer__pii_cleared", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("customer__channel", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("customer__resource_version", "INTEGER", mode="NULLABLE"),
            bigquery.SchemaField("customer__deleted", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("customer__object", "STRING", mode="NULLABLE"),# checked
            bigquery.SchemaField("customer__billing_address__first_name", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("customer__billing_address__last_name", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("customer__billing_address__email", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("customer__billing_address__company", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("customer__billing_address__line1", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("customer__billing_address__city", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("customer__billing_address__state_code", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("customer__billing_address__state", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("customer__billing_address__country", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("customer__billing_address__zip", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("customer__billing_address__validation_status", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("customer__billing_address__object", "STRING", mode="NULLABLE"),# checked
            bigquery.SchemaField("customer__card_status", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("customer__promotional_credits", "INTEGER", mode="NULLABLE"),
            bigquery.SchemaField("customer__refundable_credits", "INTEGER", mode="NULLABLE"),
            bigquery.SchemaField("customer__excess_payments", "INTEGER", mode="NULLABLE"),
            bigquery.SchemaField("customer__unbilled_charges", "INTEGER", mode="NULLABLE"),
            bigquery.SchemaField("customer__preferred_currency_code", "STRING", mode="NULLABLE"),# checked
            bigquery.SchemaField("customer__mrr", "INTEGER", mode="NULLABLE"),
            bigquery.SchemaField("customer__tax_providers_fields", "JSON", mode="NULLABLE"),
            bigquery.SchemaField("customer__auto_close_invoices", "STRING", mode="NULLABLE"),    
            bigquery.SchemaField("customer__cf_payment_id", "INTEGER", mode="NULLABLE")
        ]
    
    return table_schema_subscriptions