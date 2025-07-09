# CourtListener API Analysis - REST vs Webhooks for Supreme Court Data

## Executive Summary

**Recommendation**: Use **REST API with bulk data** for historical data collection (2022-2023, 2023-2024 terms) and **Webhooks** for ongoing real-time monitoring.

## API Options Comparison

### 1. REST API Approach

**Best For**: Historical data collection, batch processing, controlled data gathering

**Key Endpoints**:
- `/api/rest/v4/opinions/?cluster__docket__court=scotus` - Supreme Court opinions
- `/api/rest/v3/dockets/` - Case metadata and docket information  
- `/api/rest/v3/clusters/` - Opinion clusters (majority, dissent, concurrence groupings)
- `/api/rest/v3/oral-arguments/` - Oral argument recordings and transcripts

**Advantages**:
- ✅ **Perfect for our Phase 1 needs** - Historical data collection
- ✅ **Structured data access** - Query specific terms, date ranges, justices
- ✅ **Predictable costs** - Rate limited to 1,000 queries/hour/endpoint
- ✅ **Filtering capabilities** - Can target specific Supreme Court data only
- ✅ **Bulk data option** - CSV/JSON dumps for large datasets
- ✅ **No ongoing subscription fees** - Pay-per-use model

**Disadvantages**:
- ❌ **Rate limiting** - 1,000 queries/hour may require patience for large datasets
- ❌ **Polling required** - Must regularly check for updates
- ❌ **No real-time updates** - Delayed notification of new decisions

### 2. Webhook Approach

**Best For**: Real-time monitoring, automated alerts, ongoing data updates

**Key Features**:
- **Event-driven** - Pushes data when Supreme Court decisions published
- **Reliable delivery** - Exponential backoff, up to 7 retries
- **Idempotency** - UUID prevents duplicate processing
- **JSON payload** - Structured data delivery

**Advantages**:
- ✅ **Real-time updates** - Immediate notification of new decisions
- ✅ **No polling overhead** - Data pushed to you automatically  
- ✅ **Reliable delivery** - Built-in retry mechanisms
- ✅ **Efficient** - No wasted API calls checking for updates

**Disadvantages**:
- ❌ **Subscription fees** - Non-profit charges organizations for webhook service
- ❌ **Infrastructure required** - Need webhook endpoint server
- ❌ **Not for historical data** - Only notifies about new events
- ❌ **Less control** - Can't query specific historical data

## Recommended Implementation Strategy

### Phase 1: Historical Data Collection (Current Need)
**Use REST API + Bulk Data**

```bash
# Example Supreme Court opinion query
curl -H "Authorization: Token YOUR_TOKEN" \
  "https://www.courtlistener.com/api/rest/v4/opinions/?cluster__docket__court=scotus&date_created__gte=2022-10-01&date_created__lt=2023-07-01"
```

**Implementation Plan**:
1. **Authenticate** - Get API token from CourtListener
2. **Query by term** - Filter by date ranges for 2022-2023 and 2023-2024
3. **Collect systematically**:
   - Dockets (case metadata)
   - Opinion clusters (decision groupings)
   - Individual opinions (majority, dissent, concurrence)
   - Oral arguments (transcripts, audio)
4. **Respect rate limits** - 1,000 queries/hour, implement backoff
5. **Store locally** - Build our data structure as defined in ARCHITECTURE.md

### Phase 2: Real-time Monitoring (Future)
**Add Webhooks for ongoing updates**

**Implementation Plan**:
1. **Set up webhook endpoint** - Server to receive notifications
2. **Subscribe to Supreme Court events** - New decisions, oral arguments
3. **Process incoming data** - Update local database, trigger predictions
4. **Maintain historical API** - Keep REST API for detailed queries

## Technical Specifications

### Authentication
```bash
# Token-based authentication required
curl -H "Authorization: Token YOUR_TOKEN" \
  "https://www.courtlistener.com/api/rest/v3/dockets/"
```

### Rate Limiting
- **REST API**: 1,000 queries/hour/endpoint/user
- **Webhooks**: No rate limits (push-based)
- **Bulk Data**: No rate limits (download-based)

### Data Format
- **REST API**: JSON responses with pagination
- **Webhooks**: JSON events with payload structure
- **Bulk Data**: CSV/JSON files

### Supreme Court Specific Features
- **Court filter**: `court=scotus` or `court__id=scotus`
- **Date filtering**: `date_created__gte=2022-10-01`
- **Opinion types**: Automatically grouped by clusters
- **Oral arguments**: Largest collection available

## Cost Considerations

### REST API
- **Free tier**: 1,000 queries/hour
- **Paid tier**: Contact for higher limits
- **Bulk data**: Free download access

### Webhooks
- **Subscription fee**: Paid service for organizations
- **Infrastructure**: Server costs for webhook endpoint
- **Reliability**: Built-in retry mechanisms included

## Implementation Priority

**Immediate (Phase 1)**:
1. ✅ Set up REST API authentication
2. ✅ Build data collection scripts for 2022-2023 term
3. ✅ Test with single case (Arellano v. McDonough)
4. ✅ Scale to full term collection

**Future (Phase 2)**:
1. ⏳ Evaluate webhook costs vs benefits
2. ⏳ Set up webhook infrastructure if justified
3. ⏳ Implement hybrid approach (REST + Webhooks)

## Conclusion

**For ClaudeScotus Phase 1**: REST API is the clear choice for historical data collection. It provides the structured access we need for 2022-2023 and 2023-2024 terms with predictable costs and full control over data collection.

**For Future Development**: Webhooks become valuable for real-time prediction system deployment, but are not needed for current development phase.

**Next Steps**: 
1. Register for CourtListener API token
2. Implement REST API data collection system
3. Test with existing case data structure
4. Scale to full term collection

---

**Analysis Date**: 2025-01-09  
**Recommendation**: REST API for Phase 1, evaluate webhooks for Phase 2  
**Priority**: High - needed for data collection system implementation